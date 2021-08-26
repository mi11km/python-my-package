"""
全探索 Brute-force search : 「全てのあり得る通り数を探索する」
"""


def factorization(number: int) -> int:
    """ number を素因数分解し約数の個数"""
    result = 0
    for num in range(1, number + 1):
        if number % num == 0:
            result += 1
    return result


def b_105():
    n = int(input())
    result = 0
    if not (n < 105):
        for number in range(105, n + 1, 2):
            if factorization(number) == 8:
                result += 1
    print(result)


if __name__ == '__main__':
    b_105()
