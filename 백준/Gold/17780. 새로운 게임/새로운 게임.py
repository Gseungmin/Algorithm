import sys
input = sys.stdin.readline

N, K = map(int,input().split())

graph = [list(map(int,input().split())) for i in range(N)]

Dict = dict()
for i in range(N):
    for j in range(N):
        Dict[(i,j)] = []

horse = dict()

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]

#말 네게가 겹치면 끝

for i in range(K):
    x, y, k = map(int,input().split())
    x, y = x-1, y-1
    horse[i] = [x,y,k]
    Dict[(x,y)].append(i)
    
def blue(x, y, k, i):
    
    if k == 1:
        nk = 2
    if k == 2:
        nk = 1
    if k == 3:
        nk = 4
    if k == 4:
        nk = 3
    
    nx, ny = x+dx[nk], y+dy[nk]
    
    if 0<=nx<N and 0<=ny<N:
        if graph[nx][ny] == 2:
            horse[i] = [x,y,nk]
            return
        elif graph[nx][ny] == 0:
            for m in Dict[(x,y)]:
                Dict[(nx,ny)].append(m)
                d = horse[m][2]
                
                if m == i:
                    horse[m] = [nx,ny,nk]
                else:
                    horse[m] = [nx,ny,d]
                    
            Dict[(x, y)] = []
        elif graph[nx][ny] == 1:
            for m in range(len(Dict[(x,y)])-1,-1,-1):
                Dict[(nx,ny)].append(Dict[(x,y)][m])
                d = horse[Dict[(x,y)][m]][2]
                
                if m == 0:
                    horse[Dict[(x,y)][m]] = [nx,ny,nk]
                else:
                    horse[Dict[(x,y)][m]] = [nx,ny,d]
                    
            Dict[(x, y)] = []
    else:
        horse[i] = [x,y,nk]
        return
    
    return


    
    
for cnt in range(1000):

    for i in range(K):
        x, y, k = horse[i] #현재 말의 위치와 방향
        
        if Dict[(x,y)][0] == i: #맨 밑의 말인 경우만 이동
            nx, ny = x + dx[k], y + dy[k]
            if 0<=nx<N and 0<=ny<N:
                if graph[nx][ny] == 2:
                    blue(x,y,k,i)
                elif graph[nx][ny] == 1:
                    for m in range(len(Dict[(x,y)])-1,-1,-1):
                        Dict[(nx,ny)].append(Dict[(x,y)][m])
                        d = horse[Dict[(x,y)][m]][2]
                        horse[Dict[(x,y)][m]] = [nx,ny,d]
                    Dict[(x, y)] = []
                else:
                    for m in Dict[(x,y)]:
                        Dict[(nx,ny)].append(m)
                        d = horse[m][2]
                        horse[m] = [nx,ny,d]
                    Dict[(x, y)] = []
            else: #만약 다른 경우
                blue(x,y,k,i)
        
        for a in range(N):
            for b in range(N):
                if len(Dict[(a,b)]) >= 4:
                    print(cnt+1)
                    sys.exit()

print(-1)