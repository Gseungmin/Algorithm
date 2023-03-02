import sys
input = sys.stdin.readline
import copy

#1:1
#N*N, 바구니에 저장할 수 있는 물의 양은 제한이 없음
#1번 행과 N번 행 연결, 1번 열과 N번 열 연결
#(N,1)(N,2)(N-1,1)(N-1,2)에 구름 생성
#8개의 방향으로 이동

#1.구름이 방향을 가지고 S칸 이동
#2.바구니의 물의 양 증가
#3.구름이 사라짐
#4.물이 증가한 칸에 대해 물 복사 버그 시전, 물이 있는 바구니 수만큼 물의 양 증가, 이때 경계를 넘어가는 칸은 대각선이 아님
#5.물의 양이 2이상인 모든 칸에 구름이 생기고 물의 양이 2가 줄어듬, 이때 구름이 생기는 칸은 구름이 사라진 칸이 아니여야 함

#M번 이동 후에 바구니의 물의 양의 합을 구해라

N, M = map(int,input().split())

graph = [list(map(int,input().split())) for i in range(N)]

#방향 초기화
dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]

ddx = [-1,-1,1,1]
ddy = [-1,1,-1,1]

#구름 초기화
cloud = dict()
cloud[(N-1,0)] = True
cloud[(N-1,1)] = True
cloud[(N-2,0)] = True
cloud[(N-2,1)] = True

for i in range(M):
    d, s = map(int,input().split())
    
    #1, 2.구름 이동 및 물의 양 증가
    s %= N #반복 최소화
    List = []
    for x, y in cloud:
        nx, ny = x, y
        for j in range(s):
            nx, ny = nx+dx[d], ny+dy[d]
            if nx == -1:
                nx = N-1
            elif nx == N:
                nx = 0
            if ny == -1:
                ny = N-1
            elif ny == N:
                ny = 0
        graph[nx][ny] += 1
        List.append([nx,ny])
    
    cloud = dict()
    
    #4. 물이 증가한 칸에 대해 대각선 거리의 물의 바구니만큼 물 증가
    for x, y in List:
        cloud[(x,y)] = True
        for k in range(4):
            nx, ny = x+ddx[k], y+ddy[k]
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny] != 0:
                    graph[x][y] += 1
    
    #2이상인 모든 칸에 구름이 생기고 물의 양이 2가 줄어듦, 이때 구름이 생기는 칸은 3에서 구름이 생기는 칸이 아니여야 함
    new_cloud = dict()
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2:
                if (i,j) not in cloud:
                    graph[i][j] -= 2
                    new_cloud[(i,j)] = True

    cloud = new_cloud


ans = 0
for i in range(N):
    for j in range(N):
        ans += graph[i][j]

print(ans)