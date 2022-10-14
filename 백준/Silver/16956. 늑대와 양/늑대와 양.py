R, C = map(int,input().split())
graph = [list(input()) for i in range(R)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

for i in range(R):
    for j in range(C):
        if graph[i][j] == '.':
            graph[i][j] = 'D'
        if graph[i][j] == 'W':
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<R and 0<=ny<C:
                    if graph[nx][ny] == 'S':
                        print(0)
                        exit()
print(1)
for i in range(R):
    print("".join(graph[i]))