#!/usr/bin/env python
from src.basic import persistent_storage


def main():
    c = persistent_storage.CSVBasic()
    print(c.read_csv_file("test.csv"))
    print(c.read_csv_file("test.csv"))


if __name__ == "__main__":
    main()
