import pytest

from src.atcoder import algorithm

ascending_list = [1, 14, 32, 51, 51, 51, 243, 419, 750, 910]


@pytest.mark.parametrize(('threshold', 'expected'), [
    (51, 3),
    (1, 0),
    (910, 9),
    (52, 6),
    (0, 0),
    (911, 10),
    (-1, 0)
])
def test_binary_search(threshold: int, expected: int):
    assert algorithm.binary_search(threshold, ascending_list) == expected
