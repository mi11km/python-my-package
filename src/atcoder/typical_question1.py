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
    """ s が()でちゃんと閉じれてるかどうか調べる関数
        s: 00101などのビット列。 0: (, 1: )
    """
    if s.count('0') != s.count('1'):
        return ''
    is_ok = 0
    string = ""
    for parentheses in s:
        if parentheses == '0':
            string += '('
            is_ok += 1
        elif parentheses == '1':
            string += ')'
            is_ok -= 1
        if is_ok < 0:
            return ''
    if is_ok:
        return ''
    return string


def encyclopedia_of_parentheses():
    n = int(input())
    if n % 2 != 0:
        return
    bits = 0b0
    for _ in range(2 ** n):
        bits_str = str(bin(bits))[2:]
        bits_str = '0' * (n - len(bits_str)) + bits_str
        if parentheses := __is_close(bits_str):
            print(parentheses)
        bits += 0b1


def longest_circular_road():
    n = int(input())
    

if __name__ == '__main__':
    longest_circular_road()
