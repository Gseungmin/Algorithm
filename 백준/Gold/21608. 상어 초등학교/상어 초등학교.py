import sys
input = sys.stdin.readline
N = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

#그래프 초기화
graph = [[-1]*N for i in range(N)]
like = dict()
for _ in range(N**2):
    a, b, c, d, e = map(int,input().split())
    a, b, c, d, e = a-1, b-1, c-1, d-1, e-1
    
    #친한친구 넣기
    like[a] = set()
    like[a].add(b)
    like[a].add(c)
    like[a].add(d)
    like[a].add(e)
    
    #위치 구하기
    pos_x, pos_y, pos_cnt, pos_space = -1, -1, 0, 0
    for x in range(N):
        for y in range(N):
            if graph[x][y] == -1: #비어있다면
                cnt = 0
                space = 0
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k] #다음 인덱스
                    if 0<=nx<N and 0<=ny<N:
                        if graph[nx][ny] == -1:
                            space += 1
                        else:
                            v = graph[nx][ny]
                            if v in like[a]: #a가 좋아하는 숫자라면 cnt+1
                                cnt += 1
                if pos_x == -1 and pos_y == -1:
                    pos_x = x
                    pos_y = y
                    pos_cnt = cnt
                    pos_space = space
                else:
                    if cnt > pos_cnt: #cnt의 개수가 더 클때
                        pos_x = x
                        pos_y = y
                        pos_cnt = cnt
                        pos_space = space
                    elif cnt == pos_cnt: #cnt 개수가 같을때
                        if space > pos_space: #빈 공간이 더 많은 경우
                            pos_x = x
                            pos_y = y
                            pos_space = space
    graph[pos_x][pos_y] = a

Sum = 0
for x in range(N):
    for y in range(N):
        cnt = 0
        a = graph[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<N:
                b = graph[nx][ny]
                if b in like[a]:
                    cnt += 1
        if cnt == 1:
            Sum += 1
        elif cnt == 2:
            Sum += 10
        elif cnt == 3:
            Sum += 100
        elif cnt == 4:
            Sum += 1000

print(Sum)