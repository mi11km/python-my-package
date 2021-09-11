def a():
    n = int(input())
    s = input()
    if s[n - 1] == "o":
        print("Yes")
    else:
        print("No")


def b():
    words = {index: char for index, char in enumerate(list("abcdefghijklmnopqrstuvwxyz"))}
    p = list(map(int, input().split()))
    print("".join([words[i - 1] for i in p]))


b()
