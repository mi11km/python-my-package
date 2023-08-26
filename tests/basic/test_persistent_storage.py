import os

import pytest

from src.basic.persistent_storage import CSVBasic


def test_csv():
    filename = "test.csv"
    c = CSVBasic()

    c.write_csv_file(filename, c.dummy_list_data())
    assert c.read_csv_file(filename) == c.dummy_list_data()

    os.remove(c.file_path + filename)

    invalid_filename = "test.txt"
    with pytest.raises(ValueError) as err:
        c.write_csv_file(invalid_filename, c.dummy_list_data())
    assert err.type is ValueError
