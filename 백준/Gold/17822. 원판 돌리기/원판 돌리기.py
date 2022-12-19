import sys
input = sys.stdin.readline
N, M, T = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]

#현재
now = dict()
#변경후
after = dict()
for i in range(1,N+1):
    for j in range(1,M+1):
        now[(i,j)] = graph[i-1][j-1]
        after[(i,j)] = graph[i-1][j-1]

for t in range(T):
    
    #after 초기화
    after = dict()
    for x in range(1,N+1):
        for y in range(1,M+1):
            after[(x,y)] = now[(x,y)]
    
    v, d, k = map(int,input().split())
    mul = 1
    
    x = v*mul
    #first: 회전 구현
    while x <= N:
        for y in range(1,M+1):
            if d == 0: #시계방향
                ny = (y+k)%M
                if ny == 0:
                    ny = M
                after[(x,ny)] = now[(x,y)]
            elif d == 1: #반시계 방향
                ny = (M+(y-k))%M
                if ny == 0:
                    ny = M
                after[(x,ny)] = now[(x,y)]
        mul += 1
        
        x = v*mul

    dx = [0,0,1]
    dy = [-1,1,0]
    destroy = dict()
    #Second-1: 인접한 수 모두 제거
    for x in range(1,N+1):
        for y in range(1,M+1):
            for i in range(3):
                if x == N and i == 2:
                    continue
                nx = x + dx[i]
                ny = y + dy[i]
                if ny == 0:
                    ny = M
                elif ny == M+1:
                    ny = 1
                if after[(x,y)] != False and after[(nx,ny)] != False and after[(x,y)] == after[(nx,ny)]:
                    destroy[(x,y)] = True
                    destroy[(nx,ny)] = True
    
    if len(destroy) > 0:
        for x, y in destroy:
            after[(x,y)] = False
    else:
        #Second-2: 평균
        Sum = 0
        cnt = 0
        for x in range(1,N+1):
            for y in range(1,M+1):
                if after[(x,y)] != False:
                    cnt += 1
                    Sum += after[(x,y)]
        if cnt != 0:
            avg = Sum / cnt
            
    
            for x in range(1,N+1):
                for y in range(1,M+1):
                    if after[(x,y)] != False:
                        if after[(x,y)] > avg: 
                            after[(x,y)] -= 1
                        elif after[(x,y)] < avg:
                            after[(x,y)] += 1
    
    #now에 변경 사항 반영
    ans = 0
    now = dict()
    for x in range(1,N+1):
        for y in range(1,M+1):
            now[(x,y)] = after[(x,y)]
            if now[(x,y)] != False:
                ans += now[(x,y)]

print(ans)
