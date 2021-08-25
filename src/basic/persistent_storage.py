import csv
import os


# CSV: 区切り文字によってフィールドに区切られているファイル形式。スプレッドシートやDBとのデータ交換形式としてよく使われる。
class CSVBasic:
    __file_path: str = "./assets/"

    @staticmethod
    def dummy_list_data() -> list[list]:
        return [['Doctor', 'No'], ['Rosa', 'Klebb'], ['Mister', 'Big'],
                ['Auric', 'GoldFinger'], ['Ernst', 'Blofeld'], ]

    @staticmethod
    def dummy_dict_data() -> list[dict]:
        return [{'first': 'Doctor', 'second': 'No'}, {'first': 'Rosa', 'second': 'Klebb'},
                {'first': 'Mister', 'second': 'Big'}, {'first': 'Auric', 'second': 'GoldFinger'},
                {'first': 'Ernst', 'second': 'Blofeld'}]

    def validation(self, filename: str) -> None:
        if not filename.endswith('.csv'):
            raise ValueError('filename is not csv format, ', filename)
        if not os.path.exists(self.__file_path):
            os.mkdir(self.__file_path)

    def write_csv_file(self, filename: str, data: list) -> None:
        self.validation(filename)
        with open(self.__file_path + filename, 'w') as file:
            if type(data[0]) is list:
                print('list!')
                csv.writer(file).writerows(data)
            elif type(data[0]) is dict:
                print('dict!')
                writer = csv.DictWriter(file, fieldnames=['first', 'second'])
                writer.writeheader()
                writer.writerows(data)

    def read_csv_file(self, filename: str, as_dict: bool = False) -> list:
        self.validation(filename)
        with open(self.__file_path + filename, 'r') as file:
            if as_dict:
                data = [row for row in csv.DictReader(file, fieldnames=['first', 'second'])]
            else:
                data = [row for row in csv.reader(file)]
        return data


if __name__ == '__main__':
    c = CSVBasic()
    c.write_csv_file('test.csv', c.dummy_dict_data())
    print(c.read_csv_file('test.csv'))
    print(c.read_csv_file('test.csv', as_dict=True))
