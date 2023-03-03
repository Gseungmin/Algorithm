#4:26
#빨간 구슬과 파란 구슬, 빨간 구슬을 빼내는 게임
#N, M, 테두리는 막혀있음, 파란 구슬은 구멍에 들어가면 안됨
#4가지 기울이기 가능
#기울이는 동작을 그만두는 것은 더이상 구슬이 움지이지 않을때까지이다

import sys
input = sys.stdin.readline
from collections import deque

#입력조건 초기화
N, M = map(int,input().split())
graph = [list(input().rstrip()) for i in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def DFS(rx, ry, bx, by, hx, hy, cnt):
    
    #파란 구슬이 빠진 경우는 무조건 제외
    if bx == hx and by == hy:
        return
    
    #빨강 구슬만 빠진 경우 정답 출력
    if rx == hx and ry == hy:
        print(1)
        sys.exit()
        return
    
    #이미 10번 움직인 경우 뒤로 이동
    if cnt == 11:
        return
    
    #구슬 이동 방향 결정
    for i in range(4):
        
        nrx, nry, nbx, nby = rx, ry, bx, by
        
        if i == 0:
            
            if rx < bx: #rx부터 이동해야 하는 경우
            
                for nrx in range(rx,-1,-1):
                    if graph[nrx][nry] == "#": #벽만나면 직전이 마지막 이동
                        nrx += 1
                        break
                    elif graph[nrx][nry] == "O": #구멍 만나면 안으로 이동
                        break
                
                for nbx in range(bx, -1, -1):
                    if graph[nbx][nby] == "#": #벽만나면 직전이 마지막 이동
                        nbx += 1
                        break
                    elif graph[nbx][nby] == "O": #구멍 만나면 안으로 이동
                        break
                    elif nrx == nbx and nry == nby:
                        nbx += 1
                        break
                    
            else: #bx부터 이동해야 하는 경우
            
                for nbx in range(bx, -1, -1):
                    if graph[nbx][nby] == "#": #벽만나면 직전이 마지막 이동
                        nbx += 1
                        break
                    elif graph[nbx][nby] == "O": #구멍 만나면 안으로 이동
                        break
            
                for nrx in range(rx,-1,-1):
                    if graph[nrx][nry] == "#": #벽만나면 직전이 마지막 이동
                        nrx += 1
                        break
                    elif graph[nrx][nry] == "O": #구멍 만나면 안으로 이동
                        break
                    elif nrx == nbx and nry == nby:
                        nrx += 1
                        break

        elif i == 1:
            
            if rx < bx: #bx부터 이동해야 하는 경우
            
                for nbx in range(bx, N):
                    if graph[nbx][nby] == "#": #벽만나면 직전이 마지막 이동
                        nbx -= 1
                        break
                    elif graph[nbx][nby] == "O": #구멍 만나면 안으로 이동
                        break
            
                for nrx in range(rx,N):
                    if graph[nrx][ry] == "#": #벽만나면 직전이 마지막 이동
                        nrx -= 1
                        break
                    elif graph[nrx][nry] == "O": #구멍 만나면 안으로 이동
                        break
                    elif nrx == nbx and nry == nby:
                        nrx -= 1
                        break
                    
            else: #bx부터 이동해야 하는 경우
            
                for nrx in range(rx,N):
                    if graph[nrx][nry] == "#": #벽만나면 직전이 마지막 이동
                        nrx -= 1
                        break
                    elif graph[nrx][nry] == "O": #구멍 만나면 안으로 이동
                        break
                
                for nbx in range(bx, N):
                    if graph[nbx][nby] == "#": #벽만나면 직전이 마지막 이동
                        nbx -= 1
                        break
                    elif graph[nbx][nby] == "O": #구멍 만나면 안으로 이동
                        break
                    elif nrx == nbx and nry == nby:
                        nbx -= 1
                        break

        elif i == 2:
            
            if ry < by: #rx부터 이동해야 하는 경우
            
                for nry in range(ry,-1,-1):
                    if graph[nrx][nry] == "#": #벽만나면 직전이 마지막 이동
                        nry += 1
                        break
                    elif graph[nrx][nry] == "O": #구멍 만나면 안으로 이동
                        break
                
                for nby in range(by, -1, -1):
                    if graph[nbx][nby] == "#": #벽만나면 직전이 마지막 이동
                        nby += 1
                        break
                    elif graph[nbx][nby] == "O": #구멍 만나면 안으로 이동
                        break
                    elif nrx == nbx and nry == nby:
                        nby += 1
                        break
                    
            else: #bx부터 이동해야 하는 경우
            
                for nby in range(by, -1, -1):
                    if graph[nbx][nby] == "#": #벽만나면 직전이 마지막 이동
                        nby += 1
                        break
                    elif graph[nbx][nby] == "O": #구멍 만나면 안으로 이동
                        break
            
                for nry in range(ry,-1,-1):
                    if graph[nrx][nry] == "#": #벽만나면 직전이 마지막 이동
                        nry += 1
                        break
                    elif graph[nrx][nry] == "O": #구멍 만나면 안으로 이동
                        break
                    
                    elif nrx == nbx and nry == nby:
                        nry += 1
                        break
        else:
            
            if ry < by: #rx부터 이동해야 하는 경우
            
                for nby in range(by, M):
                    if graph[nbx][nby] == "#": #벽만나면 직전이 마지막 이동
                        nby -= 1
                        break
                    elif graph[nbx][nby] == "O": #구멍 만나면 안으로 이동
                        break
            
                for nry in range(ry,M):
                    if graph[nrx][nry] == "#": #벽만나면 직전이 마지막 이동
                        nry -= 1
                        break
                    elif graph[nrx][nry] == "O": #구멍 만나면 안으로 이동
                        break
                    
                    elif nrx == nbx and nry == nby:
                        nry -= 1
                        break
                    
            else: #bx부터 이동해야 하는 경우
            
                for nry in range(ry,M):
                    if graph[nrx][nry] == "#": #벽만나면 직전이 마지막 이동
                        nry -= 1
                        break
                    elif graph[nrx][nry] == "O": #구멍 만나면 안으로 이동
                        break
                
                for nby in range(by, M):
                    if graph[nbx][nby] == "#": #벽만나면 직전이 마지막 이동
                        nby -= 1
                        break
                    elif graph[nbx][nby] == "O": #구멍 만나면 안으로 이동
                        break #구멍 만나면 안으로 이동
                    elif nrx == nbx and nry == nby:
                        nby -= 1
                        break
                        
        DFS(nrx, nry, nbx, nby, hx, hy, cnt+1)

    return



for i in range(1,N-1):
    for j in range(1,M-1):
        if graph[i][j] == "R":
            rx, ry = i, j
            graph[i][j] = "."
        elif graph[i][j] == "B":
            bx, by = i, j
            graph[i][j] = "."
        elif graph[i][j] == "O":
            hx, hy = i, j

#완전 탐색 시작
DFS(rx, ry, bx, by, hx, hy, 1)

#빨간 구슬을 빼내지 못하고 종료하는 종료조건
print(0)