import sys
input = sys.stdin.readline

#입력 초기화
R, C = map(int,input().split())
graph = [list(input().rstrip()) for i in range(R)]
move = list(input().rstrip())

#아두이노 이동경로 초기화
dx = [0,1,1,1,0,0,0,-1,-1,-1]
dy = [0,-1,0,1,-1,0,1,-1,0,1]

#종수 아두이노 이동 초기화
for i in range(len(move)):
    move[i] = int(move[i])
    
#아두이노 위치 초기화
x, y = 0, 0
crazy = []
for i in range(R):
    for j in range(C):
        if graph[i][j] == "I":
            x, y = i, j
        elif graph[i][j] == "R":
            crazy.append([i,j])

cnt = 0 #종수의 이동 횟수
for m in range(len(move)):
    
    #Condition1 종수의 이동
    nx, ny = x+dx[move[m]], y+dy[move[m]]
    x, y = nx, ny
    cnt += 1
    
    #Condition2 아두이노 위치가 겹치면 종료
    for i, j in crazy:
        if nx == i and ny == j: #만약 겹치면
            print("kraj "+str(cnt))
            sys.exit()
    
    #Condition3 미친 아두이노가 종수에 가깝게 이동
    Dict = dict()
    for h in range(len(crazy)):
        i, j = crazy[h]
        dist = int(1e9)
        ni, nj = -1, -1
        for k in range(1,len(dx)):
            if k != 5: #미친 아두이노가 멈춰있는 경우는 없음
                a, b = i+dx[k], j+dy[k]
                if 0<=a<R and 0<=b<C:
                    d = abs(a-nx) + abs(b-ny) #종수와 차이나는 거리
                    if dist > d:
                        dist = d
                        ni, nj = a, b
        if ni == nx and nj == ny: #만약 아두이노가 겹치면
            print("kraj "+str(cnt))
            sys.exit()
        
        if dist != int(1e9): #이동 했으면
            crazy[h] = [ni , nj] #미친 아두이노 이동
            
            if (ni, nj) in Dict: #미친 아두이노 위치 정리
                Dict[(ni,nj)] += 1
            else:
                Dict[(ni,nj)] = 1
    
    #살아남은 미친 아두이노 초기화
    new_craze = []
    for i, j in crazy:
        if Dict[(i,j)] <= 1:
            new_craze.append([i,j])
    crazy = new_craze
    
    #그래프 다시 초기화
    for i in range(R):
        for j in range(C):
            graph[i][j] = "."
    
    graph[nx][ny] = "I"
    for i,j in crazy:
        graph[i][j] = "R"

for i in graph:
    print("".join(i))