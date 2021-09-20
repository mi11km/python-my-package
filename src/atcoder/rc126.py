def cal_max(n2, n3, n4: int) -> int:
    counter = 0
    while n3 % 2 == 0 and n3 != 0:
        if n4 > 0:
            n3 -= 2
            n4 -= 1
            counter += 1
            continue
        elif n2 >= 2:
            n2 -= 2
            n3 -= 2
            counter += 1
            continue
    while n4 >= 2:
        if n2 > 0:
            n4 -= 2
            n2 -= 1
            counter += 1
        else:
            break
    return counter


def a():
    t = int(input())
    for _ in range(t):
        n2, n3, n4 = map(int, input().split())
        print(cal_max(n2, n3, n4))


a()
