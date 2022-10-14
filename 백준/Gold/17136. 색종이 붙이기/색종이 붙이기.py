import sys
input = sys.stdin.readline
graph = [list(map(int,input().split())) for i in range(10)]
Set = set()
for i in range(10):
    for j in range(10):
        if graph[i][j] == 1:
            Set.add((i,j))

INF = int(1e9)
ans = [INF]
cnt = [0]*6
true = set()
def RC(total):
    if total >= ans[0]:
        return
    if len(true) == len(Set):
        ans[0] = min(ans[0],total)
        return
    for i in range(10):
        for j in range(10):
            if graph[i][j] == 1 and (i,j) not in true:
                for k in range(5,0,-1):
                    if cnt[k] < 5 and i+(k-1) < 10 and j+(k-1) < 10:
                        check = 0
                        for x in range(i,i+k):
                            for y in range(j,j+k):
                                if graph[x][y] != 1 or (x,y) in true:
                                    check = 1
                                    break
                            if check == 1:
                                break
                        if check == 0:
                            for x in range(i,i+k):
                                for y in range(j,j+k):
                                    true.add((x,y))
                            cnt[k] += 1
                            RC(total+1)
                            cnt[k] -= 1
                            for x in range(i,i+k):
                                for y in range(j,j+k):
                                    true.discard((x,y))
                return
    return
RC(0)
if ans[0] == INF:
    print(-1)
else:
    print(ans[0])