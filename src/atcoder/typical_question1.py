import sys
from collections import deque

input = sys.stdin.readline


def yokan_party():
    # step1: input
    n, length = map(int, input().split())
    div_count = int(input())
    div_positions = list(map(int, input().split()))

    # step2: 答えで二分探索
    left, right = -1, length + 1
    while right - left > 1:
        middle = left + int((right - left) / 2)  # オーバーフロー対策
        count, pre = 0, 0
        for div_position in div_positions:
            if div_position - pre >= middle and length - div_position >= middle:
                count += 1
                pre = div_position
        if count >= div_count:
            left = middle
        else:
            right = middle
    print(left)


def __is_close(s: str) -> str:
    """s が()でちゃんと閉じれてるかどうか調べる関数
    s: 00101などのビット列。 0: (, 1: )
    """
    if s.count("0") != s.count("1"):
        return ""
    is_ok = 0
    string = ""
    for parentheses in s:
        if parentheses == "0":
            string += "("
            is_ok += 1
        elif parentheses == "1":
            string += ")"
            is_ok -= 1
        if is_ok < 0:
            return ""
    if is_ok:
        return ""
    return string


def encyclopedia_of_parentheses():
    n = int(input())
    if n % 2 != 0:
        return
    bits = 0b0
    for _ in range(2**n):
        bits_str = str(bin(bits))[2:]
        bits_str = "0" * (n - len(bits_str)) + bits_str
        if parentheses := __is_close(bits_str):
            print(parentheses)
        bits += 0b1


# 何故か実行時エラーになる 再帰数の制限？
def __depth_first_search(road: dict[int, list[int]], root: int, counter: int,
                         result: list):
    if root not in road.keys():
        if result[0] < counter:
            result[0] = counter
    else:
        counter += 1
        next_road = road.copy()
        del next_road[root]
        for next_city in road[root]:
            __depth_first_search(next_road, next_city, counter, result)


def longest_circular_road():
    n = int(input())
    roads: dict[int, list[int]] = {}
    for city in range(1, n + 1):
        roads[city] = []
    for _ in range(n - 1):
        a, b = map(int, input().split())
        roads[a].append(b)
        roads[b].append(a)
    # result = [0]
    # for root in roads.keys():
    #     if len(roads[root]) == 1:
    #         __depth_first_search(roads, root, 0, result)
    # print(result[0])
    _ = deque([0, -1, 0])


if __name__ == "__main__":
    longest_circular_road()
