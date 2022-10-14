import sys
input = sys.stdin.readline
N = int(input())
List = list(map(int,input().split()))
check = 0
for i in range(N):
    if List[i] >= 0:
        check = 1
        break
if check == 0 or N == 1:
    print(max(List))
    sys.exit()
DL = [0]*N
DL[0] = max(0,List[0])
DR = [0]*N
DR[N-1] = max(0,List[N-1])
for i in range(1,N):
    DL[i] = max(0,List[i]+DL[i-1])
for i in range(N-2,-1,-1):
    DR[i] = max(0,List[i]+DR[i+1])
Max = max(DL)
for i in range(N):
    if i == 0:
        Max = max(Max, DR[i+1])
    elif i == N-1:
        Max = max(Max, DL[i-1])
    else:
        Max = max(Max, DL[i-1]+DR[i+1])
print(Max)