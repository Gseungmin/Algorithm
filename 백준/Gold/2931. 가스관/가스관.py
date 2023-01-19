import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int,input().split())
graph = [list(input().rstrip()) for i in range(N)]

direct = [[1,3],[2,4],[1,2,3,4],[2,3],[1,2],[1,4],[3,4]]
shape = ["|","-","+","1","2","3","4"]

block = dict()
for i in range(7):
    block[shape[i]] = direct[i]
    
dx = [0,-1,0,1,0]
dy = [0,0,1,0,-1]

for x in range(N):
    for y in range(M):
        if graph[x][y] == ".":
            for case in range(1,8):
                
                check = True
                Set = set()
                
                #case 별로 연결 가능한지 확인
                for d in block[shape[case-1]]:
                    Set.add(d)
                    nx, ny = x+dx[d], y+dy[d]
                    if 0<=nx<N and 0<=ny<M:
                        if graph[nx][ny] == ".": #연결이 불가능한 경우
                            check = False
                            break
                        if graph[nx][ny] == "M" or graph[nx][ny] == "Z":
                            continue
                        nd = (d+2)%4
                        if nd == 0:
                            nd = 4
                        if nd not in block[graph[nx][ny]]: #연결이 불가능한 경우
                            check = False
                            break
                    else: #위 아래에 연결이 불가능 한 경우
                       check = False
                       break
                
                #주위에서 연결이 가능한지 확인
                for k in range(1,5):
                    if k in Set:
                        continue
                    Set.add(k)
                    nx = x + dx[k]
                    ny = y + dy[k]
                    reverse_k = (k+2)%4
                    if reverse_k == 0:
                        reverse_k = 4
                    if 0<=nx<N and 0<=ny<M:
                        if graph[nx][ny] != "." and graph[nx][ny] != "M" and graph[nx][ny] != "Z":
                            if reverse_k in block[graph[nx][ny]]:
                                check = False
                                break
                
                if check == True:
                    print(x+1, y+1, shape[case-1])
                    sys.exit()