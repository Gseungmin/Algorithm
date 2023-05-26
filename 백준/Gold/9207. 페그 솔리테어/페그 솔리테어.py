import sys
input = sys.stdin.readline
import itertools

#12:30
#이차원 격자, 수직 및 수평 수평으로 인접한 핀을 넘어 다음 칸으로 이동
#해당 인접한 핀은 제거됨
#핀의 개수 최소화
#판의 격자 수는 50
#매번 핀을 찾아서(50) * 모든 경우시도(8!)

T = int(input())


#pin은 핀 위치 정보 담은 배열
#check 인덱스 기반으로 제거된 핀인지 판단
#have는 map 형태로 핀 위치 정보를 담음
def RC(pin, check, have, dx, dy, N, M, move, ans):
    
    pos = False
    for i in range(len(pin)):
        x, y = pin[i]
        
        if check[i] == False:
            continue
        
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            
            if (nx, ny) in have: #점프 가능
                nnx, nny = nx+dx[k], ny+dy[k] #이동 하려는 경로
                if 0<=nnx<N and 0<=nny<M:
                    if graph[nnx][nny] != "#":
                        if (nnx, nny) not in have: #해당 경로로 이동 가능한 경우
                            pos = True
                            j = have[(nx,ny)]
                            have.pop((nx, ny))
                            have.pop((x,y))
                            have[(nnx, nny)] = i
                            pin[i][0], pin[i][1] = nnx, nny
                            check[j] = False
                            move[0] += 1
                            
                            RC(pin, check, have, dx, dy, N, M, move, ans)
                            
                            move[0] -= 1
                            pin[i][0], pin[i][1] = x, y
                            check[j] = True
                            have.pop((nnx, nny))
                            have[(nx, ny)] = j
                            have[(x, y)] = i
    
    if pos == False:
        p = 0
        for i in range(len(pin)):
            if check[i] == True:
                p += 1
        if ans[0] == -1:
            ans[0], ans[1] = p, move[0]
        else:
            if ans[0] > p:
                ans[0] = p
                ans[1] = move[0]
            elif ans[0] == p:
                ans[1] = min(ans[1], move[0])
    
    return

for _ in range(T):
    
    #입력조건
    graph = []
    for i in range(5):
        graph.append(list(input().rstrip()))
    
    if _ != T-1:
        space = input()
    
    N = len(graph)
    M = len(graph[0])
    
    ans = [-1, -1]
    move = [0]
    
    #핀의 초기 위치 확보
    pin = []
    check = []
    have = dict()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(N):
        for j in range(M):
            if graph[i][j] == "o":
                pin.append([i,j])
                check.append(True)
                have[(i,j)] = len(pin)-1
    
    #만약 핀이 하나도 없거나 하나만 있는 경우 종료조건
    if len(pin) == 0 or len(pin) == 1:
        print(len(pin), 0)
        continue
    
    RC(pin, check, have, dx, dy, N, M, move, ans)
    
    print(" ".join(map(str,ans)))