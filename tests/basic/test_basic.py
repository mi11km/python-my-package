import pytest
from typing import Tuple, List

from src.basic import basic


@pytest.mark.parametrize(('number', 'expected'), [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
])
def test_is_prime(number: int, expected: bool):
    assert basic.is_prime(number) == expected


@pytest.fixture(scope='function')
def txt(tmpdir) -> str:
    """ テスト用のテキストファイル生成 fixture """
    # 前処理
    tmp_file = tmpdir.join('test.txt')
    with tmp_file.open('w') as f:
        for number in [2, 5, 2, 6, 1, 9]:
            f.write(f'{number}\n')

    yield str(tmp_file)

    # 後処理
    tmp_file.remove()


@pytest.fixture(scope='function')
def txt_and_list(txt) -> Tuple[str, List[int]]:
    yield txt, [1, 2, 2, 5, 6, 9]


def test_load_numbers_sorted(txt_and_list):
    assert basic.load_numbers_sorted(txt_and_list[0]) == txt_and_list[1]


def test_print_hello(capsys):
    basic.print_hello()
    out, _ = capsys.readouterr()
    assert out == (
        'Hello, world!\n'
    )
