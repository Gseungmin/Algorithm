graph = [list(input()) for i in range(12)]

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = 0
while 1:
    cnt = 0
    true = [[False]*6 for i in range(12)]
    for x in range(12):
        for y in range(6):
            if graph[x][y] != "." and true[x][y] == False:
                k = graph[x][y]
                queue = deque()
                queue.append([x,y])
                true[x][y] = True
                List = []
                while queue:
                    a, b = queue.popleft()
                    List.append([a,b])
                    for i in range(4):
                        nx = a + dx[i]
                        ny = b + dy[i]
                        if 0<=nx<12 and 0<=ny<6:
                            if graph[nx][ny] == k and true[nx][ny] == False:
                                true[nx][ny] = True
                                queue.append([nx,ny])
                if len(List) >= 4:
                    cnt += len(List)
                    for i, j in List:
                        graph[i][j] = "."
    if cnt == 0:
        print(ans)
        break
    ans += 1
    for i in range(6):
        j, k = 11, 10
        while k >= 0:
            if graph[j][i] == ".":
                if graph[k][i] != ".":
                    graph[j][i], graph[k][i] = graph[k][i], "."
                    j -= 1
                    k -= 1
                else:
                    k -= 1
            else:
                j -= 1
                k = min(k,j-1)