import sys
input = sys.stdin.readline
N = int(input())
parrent = list(map(int, input().split()))
tree = [[] for i in range(N)]

for i in range(1, N):
    tree[parrent[i]].append(i)

time = [False]*N

def DP(x):
    nx_time = []
    for nx in tree[x]:
        DP(nx)
        nx_time.append(time[nx])
    if not tree[x]:
        nx_time.append(0)
    nx_time.sort(reverse=True)
    need_time = [nx_time[i]+i+1 for i in range(len(nx_time))]
    time[x] = max(need_time)
    return
    
DP(0)
print(time[0]-1)