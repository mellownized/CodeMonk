# Author : Tonmoy M
# GitHub : https://qinetique.github.io
# Problem : Monk and Inversions
# Domain : Hackerearth

T = int(input())
for i in range(T):
    N = int(input())
    M = []
    for j in range(N):
        P = list(map(int, input().split()))
        M.append(P)
    v = 0
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(N):
                    if a <= c and b <= d:
                        if M[a][b] > M[c][d]:
                            v += 1
    print(v)
