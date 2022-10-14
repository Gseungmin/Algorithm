import sys
input = sys.stdin.readline
N, K = map(int,input().split())
List = ['B']*N
Sum = 0
count = N
i = 0
j = 1
while i < N:
    if K >= Sum + count - j:
        Sum += count - j
        List[i] = 'A'
        if K == Sum:
            print("".join(List))
            sys.exit()
        j += 1
    i += 1
    count -= 1
print(-1)