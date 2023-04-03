#1:27
#정육면체 어항, N개의 어항을 가짐, 어항에는 물고기 한마리씩 존재
#1. 물고기 수가 가장 적은 어항에 한마리 집어넣음, 여러개라면 모두 한마리씩 집어넣음
#2. 가장 왼쪽의 어항을 오른쪽 어항 위로 쌓아올림
#3. 2개이상 쌓인 어항을 공중부양시킨 후 90도 회전 후 위에 쌓음, 이는 공중부양시킨 어항중 가장 오른쪽 어항이 바닥이 있을때까지 반복
#4. d = 두 어항의 차이//5, 물고기 수가 많은 곳의 물고기 d마리를 적은 곳으로 보냄
#5. 어항 1열로 정렬
#6. N//2개를 180도 회전 후 위로 올리기 2번 반복
#7. 다시 일렬 정렬

#가장 많은 물고기와 적은 물고기 어항의 차이가 K이하일때 몇번 정리해야하는가

import sys
input = sys.stdin.readline
import copy
N, K = map(int,input().split()) #N은 4의 배수
List = list(map(int,input().split()))

#그래프 초기화
graph = dict()
for i in range(N):
    graph[(0,i)] = List[i]
    
dx = [1,0]
dy = [0,1]

cnt = 0
while 1:
    
    #1. 물고기 수가 가장 작은 어항 찾아 한마리 집어넣기
    fish_num = dict()
    Min = int(1e9)
    Max = -1
    for i in range(N):
        if graph[(0,i)] not in fish_num:
            fish_num[graph[(0,i)]] = []
        fish_num[graph[(0,i)]].append(i)
        Min = min(Min, graph[(0,i)])
        Max = max(Max, graph[(0,i)])
    
    #종료조건
    if Max-Min <= K:
        print(cnt)
        sys.exit()
    
    for i in fish_num[Min]:
        graph[(0,i)] += 1
    
    #2. 가장 왼쪽의 어항을 오른쪽 어항 위로 쌓아올림
    graph[(1,0)] = graph[(0,0)]
    for i in range(1,N):
        graph[(0,i-1)] = graph[(0,i)]
    graph.pop((0,N-1))
    
    #3. 2개이상 쌓인 어항을 공중부양시킨 후 90도 회전 후 위에 쌓음, 이는 공중부양시킨 어항중 가장 오른쪽 어항이 바닥이 있을때까지 반복
    m = 0

    while 1:
        #2개 이상 쌓인 어항 찾기
        more_two = []
        for i in range(N):
            if (0,i) not in graph:
                break
            if (1,i) in graph:
                more_two.append(i)
            else:
                break
            
        #2개이상 어항 공중 부양 후 90도 회전
        for i in range(N+1):
            if (0,i) not in graph:
                width = i
                break
        
        for i in range(N+1):
            if (i,0) not in graph:
                height = i
                break
        
        dif = width-len(more_two)
        if height > dif: #쌓을 수 있는지 판단, 높이가 더 길면 쌓을 수 없음
            break
        
        sw = len(more_two)
        
        new_graph = dict() #그래프 회전
        for i in more_two:
            for j in range(height):
                new_graph[(sw-1-i+1,j)] = graph[(j,i)] #위로 올라갈 그래프
        
        for i in range(sw,width):
            new_graph[(0,i-sw)] = graph[(0,i)]
        
        graph = copy.deepcopy(new_graph)

    #4. d = 두 어항의 차이//5, 물고기 수가 많은 곳의 물고기 d마리를 적은 곳으로 보냄
    move = dict()
    
    for i in range(N):
        for j in range(N):
            if (i,j) not in graph:
                continue
            if (i,j) not in move:
                move[(i,j)] = 0
            for k in range(2):
                nx, ny = i+dx[k], j+dy[k]
                if (nx,ny) in graph:
                    if (nx,ny) not in move:
                        move[(nx,ny)] = 0
                    dif = abs(graph[(i,j)]-graph[(nx,ny)])//5
                    
                    if graph[(i,j)] > graph[(nx,ny)]:
                        move[(i,j)] -= dif
                        move[(nx,ny)] += dif
                    
                    if graph[(i,j)] < graph[(nx,ny)]:
                        move[(i,j)] += dif
                        move[(nx,ny)] -= dif
    
    for i in range(N):
        for j in range(N):
            if (i,j) in move:
                graph[(i,j)] += move[(i,j)]
    
    #5. 어항 1열로 정렬
    count = 0
    new_graph = dict()
    for j in range(N):
        for i in range(N):
            if (i,j) in graph:
                new_graph[(0,count)] = graph[(i,j)]
                count += 1
    
    graph = copy.deepcopy(new_graph)
    
    #6. N//2개를 180도 회전 후 위로 올리기 2번 반복
    #첫번째 반 자르기
    for i in range(N//2):
        graph[(1,i)] = graph[(0,N//2-1-i)]
    for i in range(N//2):
        graph[(0,i)] = graph[(0,N//2+i)]
        graph.pop((0,N//2+i))
    
    #두번째 반 자르기
    for i in range(N//4):
        graph[(2,i)] = graph[(1,N//4-1-i)]
        graph[(3,i)] = graph[(0,N//4-1-i)]
    for i in range(N//4):
        graph[(0,i)] = graph[(0,N//4+i)]
        graph[(1,i)] = graph[(1,N//4+i)]
        graph.pop((0,N//4+i))
        graph.pop((1,N//4+i))
        
    #4. d = 두 어항의 차이//5, 물고기 수가 많은 곳의 물고기 d마리를 적은 곳으로 보냄
    move = dict()
    
    for i in range(N):
        for j in range(N):
            if (i,j) not in graph:
                continue
            if (i,j) not in move:
                move[(i,j)] = 0
            for k in range(2):
                nx, ny = i+dx[k], j+dy[k]
                if (nx,ny) in graph:
                    if (nx,ny) not in move:
                        move[(nx,ny)] = 0
                    dif = abs(graph[(i,j)]-graph[(nx,ny)])//5
                    
                    if graph[(i,j)] > graph[(nx,ny)]:
                        move[(i,j)] -= dif
                        move[(nx,ny)] += dif
                    
                    if graph[(i,j)] < graph[(nx,ny)]:
                        move[(i,j)] += dif
                        move[(nx,ny)] -= dif
    
    for i in range(N):
        for j in range(N):
            if (i,j) in move:
                graph[(i,j)] += move[(i,j)]
        
    #7. 어항 1열로 정렬
    count = 0
    new_graph = dict()
    for j in range(N):
        for i in range(N):
            if (i,j) in graph:
                new_graph[(0,count)] = graph[(i,j)]
                count += 1
    
    graph = copy.deepcopy(new_graph)
    
    cnt += 1