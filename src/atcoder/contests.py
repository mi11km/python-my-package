def a():
    x = int(input())
    if 0 <= x < 40:
        print(40 - x)
    elif 40 <= x < 70:
        print(70 - x)
    elif 70 <= x < 90:
        print(90 - x)
    else:
        print("expert")


def b():
    s = [input() for _ in range(3)]
    t = input()
    for n in t:
        print(s[int(n) - 1], end="")
    print()


def cmp_str(a, b, condition):
    if len(a) < len(b):
        short, long = a, b
    else:
        short, long = b, a
    if long.startswith(short):
        return short
    for i, c in enumerate(short):
        if condition[c] < condition[long[i]]:
            return short
    return long


def c():
    x = input()
    n = int(input())
    s = [input() for _ in range(n)]
    dict_hash = {}
    for index, char in enumerate(x):
        dict_hash[char] = index
    s = sorted(s, key=lambda x: dict_hash[x[0]])
    is_swapped = True
    while is_swapped:
        is_swapped = False
        for i, string in enumerate(s):
            if i == 0:
                continue
            if cmp_str(string, s[i - 1], condition=dict_hash) == string:
                s[i], s[i - 1] = s[i - 1], s[i]
                is_swapped = True
    for ss in s:
        print(ss)


c()
