import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
if N == 1 or N == 2:
    print(0)
    sys.exit()

ans = -1
for i in range(-1,2):
    for j in range(-1,2):
        true = 0
        List = []
        cnt = abs(i) + abs(j)
        List.append(A[0] + i)
        List.append(A[1] + j)
        dif = List[-1] - List[-2]
        for k in range(2, len(A)):
            if A[k] - List[-1] == dif:
                List.append(A[k])
            elif (A[k]+1) - List[-1] == dif:
                List.append(A[k]+1)
                cnt += 1
            elif (A[k]-1) - List[-1] == dif:
                List.append(A[k]-1)
                cnt += 1
            else:
                true = 1
                break
        if true == 1:
            continue
        if ans == -1:
            ans = cnt
        else:
            ans = min(ans, cnt)
print(ans)