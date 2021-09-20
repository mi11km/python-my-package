# Educational DP Contest

def a_frog1():
    n = int(input())
    h = list(map(int, input().split()))
    dp = [0] * n
    for i in range(1, n):
        if i == 1:
            dp[i] = abs(h[i] - h[i - 1])
        else:
            dp[i] = min(dp[i - 2] + abs(h[i] - h[i - 2]), dp[i - 1] + abs(h[i] - h[i - 1]))
    print(dp[n - 1])


def b_frog2():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    dp = [10 ** 9] * n
    dp[0] = 0
    for i in range(n):
        for j in range(k + 1):
            if i + j < n:
                dp[i + j] = min(dp[i] + abs(h[i + j] - h[i]), dp[i + j])
    print(dp[n - 1])


def c_vacation():
    n = int(input())
    activity = [tuple(map(int, input().split())) for _ in range(n)]
    a, b, c = [0], [0], [0]
    for i in range(n):
        a.append(activity[i][0] + max(b[i], c[i]))
        b.append(activity[i][1] + max(a[i], c[i]))
        c.append(activity[i][2] + max(a[i], b[i]))
    print(max(a[-1], b[-1], c[-1]))


c_vacation()
