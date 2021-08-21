def is_prime(n: int) -> bool:
    """ n が素数かどうか判定する関数 """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for odd_number in range(3, n, 2):
        if n % odd_number == 0:
            return False
    return True


def load_numbers_sorted(txt: str) -> list[int]:
    with open(txt) as f:
        numbers = sorted(map(lambda e: int(e), f))
    return numbers


def print_hello():
    print('Hello, world!')


def is_tweeted(string: str) -> str:
    """ セイウチ演算子の例 """
    limit = 280
    if (diff := limit - len(string)) >= 0:
        return "A fitting tweet"
    else:
        return f"Went over by {abs(diff)}"
