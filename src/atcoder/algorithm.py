def binary_search(threshold: int, array: list[int]) -> int:
    """
    昇順リスト array の中で threshold 以上を満たす最小の値のインデックスを返す
    https://qiita.com/drken/items/97e37dd6143e33a64c8c
    """
    left, right = -1, len(array)
    while right - left > 1:
        middle = int((left + right) / 2)
        if array[middle] >= threshold:
            right = middle
        else:
            left = middle
    return right
