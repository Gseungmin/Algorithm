import sys
input = sys.stdin.readline
N, M, D = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
ans = [0]

target = []
for i in range(N):
    for j in range(M): 
        if graph[i][j] == 1:
            target.append([i,j])

def RC(index, cnt, List):
    if cnt == 3:
        m = attack(List)
        ans[0] = max(ans[0], len(m))
        return
    if index == (N+1)*M:
        return
    x, y = index//M, index%M
    List.append([x,y])
    RC(index+1, cnt+1, List)
    List.pop()
    RC(index+1, cnt, List)
    return

import heapq
def attack(List):
    t = 0
    x1,y1,x2,y2,x3,y3 = List[0][0], List[0][1], List[1][0], List[1][1], List[2][0], List[2][1]
    dead = set()
    while t <= N:
        List1, List2, List3 = [], [], []
        for i, j in target:
            if (i,j) in dead:
                continue
            k = i+t
            if k >= N:
                continue
            heapq.heappush(List1,([abs(x1-k)+abs(y1-j), j, i]))
            heapq.heappush(List2,([abs(x2-k)+abs(y2-j), j, i]))
            heapq.heappush(List3,([abs(x3-k)+abs(y3-j), j, i]))
        check = 0
        if List1:
            k, ty1, tx1 = List1[0]
            if k <= D:
                dead.add((tx1,ty1))
        if List2:
            k, ty2, tx2 = List2[0]
            if k <= D:
                dead.add((tx2,ty2))
        if List3:
            k, ty3, tx3 = List3[0]
            if k <= D:
                dead.add((tx3,ty3))
        t += 1
    return dead
    
RC(N*M, 0, [])
print(ans[0])