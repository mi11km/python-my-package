import csv
import os


# CSV: 区切り文字によってフィールドに区切られているファイル形式。スプレッドシートやDBとのデータ交換形式としてよく使われる。
class CSVBasic:

    def __init__(self, file_store_path: str = "./"):
        self.__file_path = file_store_path

    @property
    def file_path(self) -> str:
        return self.__file_path

    def __validation(self, filename: str) -> None:
        if not filename.endswith(".csv"):
            raise ValueError("filename is not csv format, ", filename)
        if not os.path.exists(self.__file_path):
            os.mkdir(self.__file_path)

    def write_csv_file(self, filename: str, data: list) -> None:
        self.__validation(filename)
        with open(self.__file_path + filename, "w") as file:
            if type(data[0]) is list:
                csv.writer(file).writerows(data)
            elif type(data[0]) is dict:
                writer = csv.DictWriter(file, fieldnames=["first", "second"])
                writer.writeheader()
                writer.writerows(data)

    def read_csv_file(self, filename: str) -> list[list[str]]:
        self.__validation(filename)
        with open(self.__file_path + filename, "r") as file:
            data = [row for row in csv.reader(file)]
        return data

    @staticmethod
    def dummy_list_data() -> list[list]:
        return [
            ["Doctor", "No"],
            ["Rosa", "Klebb"],
            ["Mister", "Big"],
            ["Auric", "GoldFinger"],
            ["Ernst", "Blofeld"],
        ]


if __name__ == "__main__":
    c = CSVBasic()
    c.write_csv_file("test.csv", c.dummy_list_data())
    print(c.read_csv_file("test.csv"))
    print(c.read_csv_file("test.csv"))
