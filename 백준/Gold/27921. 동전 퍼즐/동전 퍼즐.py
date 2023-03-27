#1:24

#무한 격자에 동전이 놓여있음
#최소 동전의 개수를 옮겨서 새로운 모양을 만드는 것
#A->B로 바꿀때 최소 변경 횟수
#A를 기준으로 잡고 해당 

import sys
input = sys.stdin.readline

N1, M1 = map(int,input().split())
graph1 = [list(input().rstrip()) for i in range(N1)]

N2, M2 = map(int,input().split())
graph2 = [list(input().rstrip()) for i in range(N2)]

coin1 = []
for i in range(N1):
    for j in range(M1):
        if graph1[i][j] == "O":
            coin1.append([i,j])

coin2 = []
for i in range(N2):
    for j in range(M2):
        if graph2[i][j] == "O":
            coin2.append([i,j])

#만약 동전이 없을 경우 답은 0
if len(coin1) == 0:
    print(0)
    sys.exit()

ans = int(1e9)

dif = dict()
for a in coin1:
    i, j = a #coin1의 위치
    for b in coin2:
        x, y = b #coin2의 위치
        
        #두 코인을 결정 했을때, 그래프 이동
        dif_x, dif_y = x-i, y-j
        
        if (dif_x, dif_y) in dif:
            continue
        
        dif[(dif_x,dif_y)] = True
        
        cnt = 0
        for nx in range(N1):
            for ny in range(M1):
                if graph1[nx][ny] == "O":
                    if 0<=nx+dif_x<N2 and 0<=ny+dif_y<M2: #범위내에 있을때
                        if graph2[nx+dif_x][ny+dif_y] == "O":
                            cnt += 1
        
        value = len(coin1) - cnt
        ans = min(ans,value)

print(ans)