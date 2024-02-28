#!/usr/bin/env python
import datetime
import gzip
import os
import shutil

import pandas as pd

name_map = {
    "F-H-N": [
        ["L", "2024/02/21 13:43", "2024/02/21 13:47"],
        ["S", "2024/02/21 13:47", "2024/02/21 13:51"],
        ["SS", "2024/02/21 13:51", "2024/02/21 13:54"],
        ["A", "2024/02/21 13:58", "2024/02/21 14:06"],
        ["D", "2024/02/21 14:06", "2024/02/21 14:11"],
        ["AD", "2024/02/21 14:12", "2024/02/21 14:15"],
    ],
    "F-HV-N": [
        ["L", "2024/02/21 14:21", "2024/02/21 14:25"],
        ["S", "2024/02/21 14:25", "2024/02/21 14:29"],
        ["SS", "2024/02/21 14:29", "2024/02/21 14:33"],
        ["A", "2024/02/21 14:38", "2024/02/21 14:46"],
        ["D", "2024/02/21 14:46", "2024/02/21 14:53"],
        ["AD", "2024/02/21 14:53", "2024/02/21 14:56"],
    ],
    "F-V-N": [
        ["L", "2024/02/21 15:24", "2024/02/21 15:27"],
        ["S", "2024/02/21 15:28", "2024/02/21 15:32"],
        ["SS", "2024/02/21 15:32", "2024/02/21 15:36"],
        ["A", "2024/02/21 15:39", "2024/02/21 15:47"],
        ["D", "2024/02/21 15:48", "2024/02/21 15:52"],
        ["AD", "2024/02/21 15:52", "2024/02/21 15:53"],
    ]
}
python_datetime_format = "%Y/%m/%d %H:%M"
date_format = "%Y:%m:%d:%H:%M:%S.%f"


def main():
    original_dir = "./tmp/original/"
    iPhone8 = "iPhone8"
    iPhone12pro = "iPhone12pro"
    GooglePixel4a = "GooglePixel4a"

    device_name = GooglePixel4a
    source_dir = f"./tmp/decompressedOriginal/{device_name}/"
    output_dir = f"./tmp/dist/{device_name}/"

    files = os.listdir(source_dir)
    files.sort()
    kinds = [
        f.replace(f"{device_name}-", "").replace(".ndjson", "") for f in files
    ]

    for i in range(len(files)):
        df = pd.read_json(source_dir + files[i],
                          lines=True,
                          dtype=str,
                          convert_dates=False)
        # 時刻を変換
        # df["time"] = df["time"].str.replace(":", "/", n=2)
        # df["time"] = df["time"].str.replace(":", " ", n=1)
        df["time"] = pd.to_datetime(df["time"])
        try:
            separations = name_map[kinds[i]]
            print(files[i])
            for separation in separations:
                # 分割
                start = datetime.datetime.strptime(
                    separation[1],
                    python_datetime_format) - datetime.timedelta(
                        minutes=1)  # 1分前から取得
                end = datetime.datetime.strptime(
                    separation[2],
                    python_datetime_format) + datetime.timedelta(
                        minutes=1)  # 1分後まで取得
                df_separation = df[(df["time"] >= start) & (df["time"] <= end)]

                # 時刻の形式を変換
                df_separation["time"] = df_separation["time"].dt.strftime(
                    date_format)
                df_separation["time"] = df_separation["time"].str[:-3]

                # ファイル出力
                out_filename = output_dir + device_name + "-" + kinds[
                    i] + "-" + separation[0] + ".ndjson"
                df_separation.to_json(out_filename,
                                      orient="records",
                                      lines=True)
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
