def welcome_to_atcoder():
    a = int(input())
    b, c = map(int, input().split())
    s = input()
    print(f"{a + b + c} {s}")


def product():
    a, b = map(int, input().split())
    if a * b % 2:
        print("Even")
    else:
        print("Odd")


def placing_marbles():
    # s = input()
    # print(int(s[0]) + int(s[1]) + int(s[2]))
    print(input().count("1"))


def shift_only():
    n = int(input())
    a = list(map(int, input().split()))
    is_ok, counter = True, 0
    while is_ok:
        for i in range(n):
            if a[i] % 2 != 0:
                is_ok = False
            else:
                a[i] = a[i] / 2
        if is_ok:
            counter += 1
    print(counter)


def coins():
    # a, b, c, x = int(input()), int(input()), int(input()), int(input())
    a, b, c, x = map(int, [input() for _ in range(4)])
    result = 0
    for coin500 in range(a + 1):
        for coin100 in range(b + 1):
            for coin50 in range(c + 1):
                if coin500 * 500 + coin100 * 100 + coin50 * 50 == x:
                    result += 1
    print(result)


def some_sums():
    n, a, b = map(int, input().split())
    result = 0
    for number in range(1, n + 1):
        # number_str = str(number)
        # number_sum = 0
        # for i in range(len(number_str)):
        #     number_sum += int(number_str[i])
        # if a <= number_sum <= b:
        #     result += number
        if a <= sum(list(map(int, list(str(number))))) <= b:
            result += number
    print(result)


def card_game_for_two():
    _ = int(input())
    a = sorted(list(map(int, input().split())), reverse=True)
    print(sum(a[::2]) - sum(a[1::2]))
    # a = list(map(int, input().split()))
    # a.sort()
    # alice, bob = 0, 0
    # is_alice = True
    # while a:
    #     if is_alice:
    #         alice += a.pop()
    #     else:
    #         bob += a.pop()
    #     is_alice = not is_alice
    # print(alice - bob)


def kagami_mochi():
    n = int(input())
    print(len(set(map(int, [input() for _ in range(n)]))))
    # d = []
    # for _ in range(n):
    #     d.append(int(input()))
    # print(len(set(d)))


def otoshidama():
    n, y = map(int, input().split())
    num10000, num5000, _ = y // 10000, y // 5000, y // 1000
    for i in range(num10000, -1, -1):
        if i > n:
            continue
        for j in range(num5000, -1, -1):
            if i + j > n:
                continue
            k = int((y - (i * 10000 + j * 5000)) / 1000)
            if i + j + k == n:
                print(i, j, k)
                return
    print(-1, -1, -1)


def hakutyumu():
    s = input()
    t_candidate = ["dream", "eraser", "erase"]
    while s:
        is_ok = False
        if s.startswith("dreamer"):
            is_ok = True
            if s.startswith("dreameraser"):
                s = s[11:]
            elif s.startswith("dreamerase"):
                s = s[10:]
            else:
                s = s[7:]
        else:
            for word in t_candidate:
                if s.startswith(word):
                    s = s[len(word):]
                    is_ok = True
                    break
        if not is_ok:
            print("NO")
            return
    print("YES")


def traveling():
    n = int(input())
    steps = [[0, 0, 0]]
    for i in range(n):
        steps.append(list(map(int, input().split())))
    is_ok = True
    for index, step in enumerate(steps):
        if index == 0:
            continue
        needed_steps = abs(step[1] -
                           steps[index - 1][1]) + abs(step[2] -
                                                      steps[index - 1][2])
        time = abs(step[0] - steps[index - 1][0])
        if time < needed_steps:
            is_ok = False
            break
        if (time - needed_steps) % 2 != 0:
            is_ok = False
            break
    if is_ok:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    traveling()
