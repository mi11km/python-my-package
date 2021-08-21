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


if __name__ == '__main__':
    yokan_party()
