import sys
input = sys.stdin.readline

N, M, K = map(int,input().split()) #N은 격자 크기, M은 상어의 수, K는 냄새 지속 시간

#초기화
graph = [list(map(int,input().split())) for i in range(N)]
smell = [[0]*N for i in range(N)]

who = dict()

shark = dict()
d = list(map(int,input().split()))

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            shark[graph[i][j]] = [i,j,d[graph[i][j]-1]-1]
            smell[i][j] = K
            who[(i,j)] = graph[i][j]
            
dx = [-1,1,0,0]
dy = [0,0,-1,1]

direct = [[]]

for i in range(1,M+1):
    List = [list(map(int,input().split())) for j in range(4)]
    direct.append(List)

#1000번까지 시도
for t in range(1000):

    #로직, 번호가 낮은 상어부터 시작
    for index in range(1,M+1):
        
        #만약 이미 제외된 상어면 넘어감
        if index not in shark:
            continue
        
        #해당 상어의 위치와 방향
        x, y, now_d = shark[index]
        
        check = 0 #불가
        
        pos = []
        
        #해당 상어의 우선순위 방향을 보면서 이동
        for next_d in direct[index][now_d]:
            nx = x+dx[next_d-1]
            ny = y+dy[next_d-1]
            if 0<=nx<N and 0<=ny<N:
                
                #냄새가 날 경우
                if smell[nx][ny] != 0:
                    #나의 냄새일 경우
                    if who[(nx,ny)] == index:
                        pos.append([nx,ny,next_d])
                    continue
                
                #냄새가 안나지면 이미 나보다 작은 상어가 있으면 쫓아짐
                
                if graph[nx][ny] != 0 and graph[nx][ny] < index:
                    check = 1 #잡아 먹힘
                    graph[x][y] = 0
                    shark.pop(index)
                    break
                
                #상어 이동 완료
                check = 2
                shark[index] = [nx,ny,next_d-1]
                graph[nx][ny] = index
                graph[x][y] = 0
                
                break
        
        if check == 0: #이동이 불가능했던 경우
            if pos:
                nx, ny, next_d = pos[0]
                shark[index] = [nx,ny,next_d-1]
                graph[nx][ny] = index
                graph[x][y] = 0
                smell[nx][ny] = K
                who[(nx,ny)] = index
        
    #방금 이동 제외하고 냄새 1씩 감소
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                smell[i][j] = K
                who[(i,j)] = graph[i][j]
            else:
                if smell[i][j] != 0:
                    smell[i][j] -= 1
                    if smell[i][j] == 0:
                        who.pop((i,j))
                
    
    #종료 조건
    if len(shark) == 1:
        print(t+1)
        sys.exit()

print(-1)