def a():
    n = int(input())
    s = input()
    if s[n - 1] == "o":
        print("Yes")
    else:
        print("No")


def b():
    words = {
        index: char
        for index, char in enumerate(list("abcdefghijklmnopqrstuvwxyz"))
    }
    p = list(map(int, input().split()))
    print("".join([words[i - 1] for i in p]))


def c():
    n = int(input())
    _ = [list(map(str, input().split())) for _ in range(n)]
    _ = [list(map(str, input().split())) for _ in range(n)]


c()
