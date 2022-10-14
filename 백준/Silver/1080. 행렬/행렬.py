N, M = map(int,input().split())
start = [list(map(int,list(input()))) for i in range(N)]
end = [list(map(int,list(input()))) for i in range(N)]

dx = [0,0,0,1,1,1,2,2,2]
dy = [0,1,2,0,1,2,0,1,2]

def change(x,y,dx,dy,start):
    for i in range(9):
        nx = x + dx[i]
        ny = y + dy[i]
        if start[nx][ny] == 1:
            start[nx][ny] = 0
        else:
            start[nx][ny] = 1
    return

count = 0
for i in range(N-2):
    for j in range(M-2):
        if start[i][j] != end[i][j]:
            change(i,j,dx,dy,start)
            count += 1

for i in range(N):
    for j in range(M):
        if start[i][j] != end[i][j]:
            count = -1
            break
    if count == -1:
        break
print(count)