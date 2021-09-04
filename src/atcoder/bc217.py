# l = list(map(str, input().split()))
# ll = l.copy()
# ll.sort()
#
# if l[0] == ll[0]:
#     print('Yes')
# else:
#     print('No')


# l = ['ABC', 'ARC', 'AGC', 'AHC']
# ll = [input() for _ in range(3)]
# for s in l:
#     if not s in ll:
#         print(s)


# n = int(input())
# p = list(map(int, input().split()))
# q = [0] * n
# for i, pp in enumerate(p):
#     q[pp - 1] = i + 1
# print(' '.join(list(map(str, q))))


# 処理時間オーバー　→　divided に平衡二分探索木とか使うらしい
l, q = map(int, input().split())
query = []
divided = [0, l]

for _ in range(q):
    query.append(tuple(map(int, input().split())))
for qq in query:
    if qq[0] == 1:
        # qq[1] で切る
        divided.append(qq[1])
        divided.sort()
    else:
        # qq[1] が含まれる木材の長さ出力
        left, right = -1, len(divided)
        while right - left > 1:
            middle = int((left + right) / 2)
            if divided[middle] >= qq[1]:
                right = middle
            else:
                left = middle
        print(divided[right] - divided[right - 1])

# divided = [[i for i in range(l + 1)]]
# for _ in range(q):
#     query.append(tuple(map(int, input().split())))
# for qq in query:
#     if qq[0] == 1:
#         # qq[1] で切る
#         for i, ll in enumerate(divided):
#             if qq[1] in ll:
#                 divided = divided[:i] + [[i for i in ll if i <= qq[1]]] + [[i for i in ll if i >= qq[1]]] + divided[i+1:]
#     else:
#         # qq[1] が含まれる木材の長さ出力
#         for ll in divided:
#             if qq[1] in ll:
#                 print(max(ll) - min(ll))
