import sys
input = sys.stdin.readline
graph = [list(map(int,input().split())) for i in range(5)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def reculsive(graph,x,y,dx,dy,ans,Len,num):
    if Len == 6:
        ans.add(num)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<5 and 0<=ny<5:
            reculsive(graph,nx,ny,dx,dy,ans,Len+1,num+str(graph[nx][ny]))
    return

ans = set()
for i in range(5):
    for j in range(5):
        num = str(graph[i][j])
        reculsive(graph,i,j,dx,dy,ans,1,num)
print(len(ans))