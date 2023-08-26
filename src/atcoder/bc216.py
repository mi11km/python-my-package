def d():
    n, m = map(int, input().split())
    tutu = []
    for _ in range(m):
        k = int(input())
        a = list(map(int, input().split()))
        tutu.append((k, a))

    tops = []
    for color in tutu:
        if not color[1][0] in tops:
            tops.append(color[1][0])
        else:
            pass
            # 書いてる途中で終了


def c():
    n = int(input())
    strings = []

    while n != 0:
        if n % 2 == 1:
            strings.append(("A", 1))
            n -= 1
        else:
            # cnt = format(n, 'b')[::-1].find('1')  # 2で割り切れる回数
            cnt = 0
            while n % 2 == 0:
                cnt += 1
                n = n // 2  # 整数除算 割る数が大きくなると変な結果になる
            if cnt != 0:
                strings.append(("B", cnt))

    result = ""
    for char in strings:
        result = char[0] * char[1] + result
    print(result)

    # balls = 0
    # for i in result:
    #     if i == 'A':
    #         balls += 1
    #     else:
    #         balls *= 2
    # print(balls)


def b():
    n = int(input())
    names = []
    for _ in range(n):
        name = tuple(map(str, input().split()))
        if name in names:
            print("Yes")
            break
        names.append(name)
    else:
        print("No")


def a():
    xy = input()
    x, y = xy[:-2], int(xy[-1])
    if 0 <= y <= 2:
        print(x + "-")
    elif 3 <= y <= 6:
        print(x)
    else:
        print(x + "+")
