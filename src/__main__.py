#!/usr/bin/env python
import datetime
import gzip
import json
import os
import shutil
from decimal import Decimal, getcontext

import pandas as pd

name_map = {
    "F-H-N": [
        ["L", "2024/02/21 13:43", "2024/02/21 13:48"],
        ["S", "2024/02/21 13:47", "2024/02/21 13:52"],
        ["SS", "2024/02/21 13:51", "2024/02/21 13:55"],
        ["A", "2024/02/21 13:58", "2024/02/21 14:07"],
        ["D", "2024/02/21 14:06", "2024/02/21 14:12"],
        ["AD", "2024/02/21 14:12", "2024/02/21 14:16"],
    ],
    "F-HV-N": [
        ["L", "2024/02/21 14:21", "2024/02/21 14:26"],
        ["S", "2024/02/21 14:25", "2024/02/21 14:30"],
        ["SS", "2024/02/21 14:29", "2024/02/21 14:34"],
        ["A", "2024/02/21 14:38", "2024/02/21 14:47"],
        ["D", "2024/02/21 14:46", "2024/02/21 14:54"],
        ["AD", "2024/02/21 14:53", "2024/02/21 14:57"],
    ],
    "F-V-N": [
        ["L", "2024/02/21 15:24", "2024/02/21 15:28"],
        ["S", "2024/02/21 15:28", "2024/02/21 15:33"],
        ["SS", "2024/02/21 15:32", "2024/02/21 15:37"],
        ["A", "2024/02/21 15:39", "2024/02/21 15:48"],
        ["D", "2024/02/21 15:48", "2024/02/21 15:53"],
        ["AD", "2024/02/21 15:52", "2024/02/21 15:54"],
    ],
}
python_datetime_format = "%Y/%m/%d %H:%M"
date_format = "%Y:%m:%d:%H:%M:%S.%f"

iPhone8 = "iPhone8"
iPhone12pro = "iPhone12pro"
GooglePixel4a = "GooglePixel4a"


def main():
    original_dir = "./tmp/original/"
    source_dir = lambda d: f"./tmp/decompressedOriginal/{d}/"
    output_dir = lambda d: f"./tmp/dist/{d}/"
    source_android_dir = lambda d: f"./tmp/decompressedOriginal/processed/{d}/"

    split_file(iPhone8, source_dir(iPhone8), output_dir(iPhone8))
    split_file(iPhone12pro, source_dir(iPhone12pro), output_dir(iPhone12pro))
    split_file(GooglePixel4a, source_android_dir(GooglePixel4a), output_dir(GooglePixel4a))


def process_android_data(source_dir: str, output_dir: str):
    files = os.listdir(source_dir)
    files.sort()
    duration = 0.0333333333333
    for file in files:
        print(file)
        with open(source_dir + file, "r") as f:
            lines = f.read().strip().split("\n")
            json_lines = [json.loads(line) for line in lines]

        # 時刻のミリ秒を付与
        lines = []
        some_time_lines = [json_lines[0]]
        for line in json_lines[1:]:
            if line["time"] == some_time_lines[-1]["time"]:
                some_time_lines.append(line)
                continue
            else:
                diff = 30 - len(some_time_lines)
                step = diff * duration if 0 <= diff <= 30 else 0
                for some_time_line in some_time_lines:
                    step += duration
                    some_time_line["time"] = some_time_line["time"] + str(step)[1:]
                    lines.append(some_time_line)
                some_time_lines = [line]

        # 位置情報の時刻を補完
        location_timestamp = to_unix_time(lines[0]["time"])
        lines[0]["timeStamp"] = location_timestamp
        previous_line = lines[0]
        for i in range(1, len(lines)):
            if is_same_location(previous_line, lines[i]):
                lines[i]["timeStamp"] = location_timestamp
            else:
                location_timestamp = to_unix_time(lines[i]["time"])
                lines[i]["timeStamp"] = location_timestamp
            previous_line = lines[i]

        # ファイル出力
        out_filename = output_dir + file
        with open(out_filename, "w") as f:
            for line in lines:
                f.write(json.dumps(line) + "\n")


def is_same_location(location1, location2):
    return (
            location1["altitude"] == location2["altitude"]
            and location1["latitude"] == location2["latitude"]
            and location1["longitude"] == location2["longitude"]
            and location1["horizontalAccuracy"] == location2["horizontalAccuracy"]
            and location1["verticalAccuracy"] == location2["verticalAccuracy"]
    )


def to_unix_time(time: str):
    # 2024/02/21 13:42:50.43333333333290003
    return datetime.datetime.strptime(time[:26], "%Y/%m/%d %H:%M:%S.%f").timestamp()


def split_file(device_name: str, source_dir: str, output_dir: str):
    files = os.listdir(source_dir)
    files.sort()
    kinds = [f.replace(f"{device_name}-", "").replace(".ndjson", "") for f in files]
    for i in range(len(files)):
        df = pd.read_json(source_dir + files[i], lines=True, dtype=str, convert_dates=False)
        # 時刻を変換
        if device_name == iPhone8 or device_name == iPhone12pro:
            df["time"] = df["time"].str.replace(":", "/", n=2)
            df["time"] = df["time"].str.replace(":", " ", n=1)
        df["time"] = pd.to_datetime(df["time"])
        try:
            separations = name_map[kinds[i]]
            print(files[i])
            for separation in separations:
                # 分割
                start = datetime.datetime.strptime(separation[1], python_datetime_format)
                end = datetime.datetime.strptime(separation[2], python_datetime_format)
                df_separation = df[(df["time"] >= start) & (df["time"] <= end)]

                # 時刻の形式を変換
                df_separation["time"] = df_separation["time"].dt.strftime(date_format)
                df_separation["time"] = df_separation["time"].str[:-3]

                # 型を変換
                getcontext().prec = 17
                keys = [
                    "Acceleration_x",
                    "Acceleration_y",
                    "Acceleration_z",
                    "Gyro_x",
                    "Gyro_y",
                    "Gyro_z",
                    "altitude",
                    "latitude",
                    "longitude",
                    "horizontalAccuracy",
                    "verticalAccuracy",
                    "timeStamp",
                ]
                for key in keys:
                    df_separation[key] = df_separation[key].apply(Decimal)

                # ファイル出力
                out_filename = output_dir + device_name + "-" + kinds[i] + "-" + separation[0] + ".ndjson"
                df_separation.to_json(out_filename, orient="records", lines=True)
        except KeyError:
            continue


def rename_file(source_dir: str):
    files = os.listdir(source_dir)
    for file in files:
        file_name = file
        if "iPhone10,1" in file:
            file_name = file_name.replace("iPhone10,1", "iPhone8")
        elif "iPhone13,3" in file:
            file_name = file_name.replace("iPhone13,3", "iPhone12pro")
        os.rename(source_dir + file, source_dir + file_name)


def unzip(source_dir, output_dir: str):
    files = os.listdir(source_dir)
    for file in files:
        with gzip.open(source_dir + file, "rb") as gzip_file:
            with open(output_dir + file[:-3], "wb") as decompressed_file:
                shutil.copyfileobj(gzip_file, decompressed_file)


if __name__ == "__main__":
    main()
