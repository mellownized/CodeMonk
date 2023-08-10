# Author : Tonmoy M
# Github : https://qinetique.github.io
# Problem : Monk And Rotation
# Domain : Hackerearth

# n = int(input())
for i in range(int(input())):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    eqn = k % n
    print(*(lst[n - eqn:] + lst[:n - eqn]))
