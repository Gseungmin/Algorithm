import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]

from collections import deque
city = deque()
All = []
chicken = []
ans = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            city.append([i,j])
        if graph[i][j] == 2:
            All.append([i,j])

def reculsive(M,pick,index,chicken,All,city,ans):
    if pick == M:
        dist = []
        for i in city:
            x, y = i
            check = 0
            Min = -1
            for j in chicken:
                a, b = j
                if check == 0:
                    Min = abs(x-a) + abs(y-b)
                    check = 1
                else:
                    Min = min(Min, abs(x-a) + abs(y-b))
            dist.append(Min)
        ans.append(sum(dist))
        return
    if index == len(All):
        return
    chicken.append(All[index])
    reculsive(M,pick+1,index+1,chicken,All,city,ans)
    chicken.pop()
    reculsive(M,pick,index+1,chicken,All,city,ans)
    return

reculsive(M,0,0,chicken,All,city,ans)
print(min(ans))