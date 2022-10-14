import sys
input = sys.stdin.readline
true = [0]*(10001)
N = int(input())
for i in range(N):
    true[int(input())] += 1
for i in range(10001):
    if true[i] != 0:
        while true[i] != 0:
            print(i)
            true[i] -= 1