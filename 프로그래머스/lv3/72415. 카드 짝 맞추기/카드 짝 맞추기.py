#8:24
#카드 짝 맞추기 게임, 4*4 크기, 8가지 캐릭터가 2장씩 무작위 배치
#같은 그림이면 사라지며 아니면 원래 상태로 뒷면이 보이도록 뒤집힘
#1. 커서를 이용해서 카드 선택
#2. 방향키 조작(1칸이동) + ctrl 방향키 조작(해당 방향 카드 or 마지막 칸)
#3. enter를 통해 카드 뒤집기, 2번째 카드가 뒤집힐때까지 앞면 유지, 앞면이 2장이 된 경우 그림이 같으면 사라짐, 아니면 다시 뒤집힘
#카드 앞면의 그림을 모두 알고있음, 남은 카드를 모두 제거하기 위한 횟수의 최솟값

#순서 배열을 정한 후 각 경우 최선의 경로로 삭제

import itertools
import copy
from collections import deque

#이동 방향 초기화
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#x1, y1 -> x2, y2로 이동
def BFS(x1,y1,x2,y2,test_graph):
    queue = deque()
    queue.append([x1,y1])
    true = [[-1]*4 for i in range(4)]
    true[x1][y1] = 0
    while queue:
        x, y = queue.popleft()
        
        #기본 이동
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<4 and 0<=ny<4:
                if true[nx][ny] == -1: #방문 가능하지만 방문한 적이 없는 경우
                    true[nx][ny] = true[x][y]+1
                    queue.append([nx,ny])
        
        #커서 이동
        for i in range(4):
            k = 1
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<4 and 0<=ny<4:
                while test_graph[nx][ny] == 0:
                    k += 1
                    sx, sy = nx, ny
                    nx, ny = x+dx[i]*k, y+dy[i]*k
                    if 0<=nx<4 and 0<=ny<4:
                        continue
                    else:
                        nx, ny = sx, sy
                        break
                if true[nx][ny] == -1:
                    true[nx][ny] = true[x][y]+1
                    queue.append([nx,ny])
                
        if true[x2][y2] != -1:
            break
    return true[x2][y2]

def RC(r,c,index,test_graph, arr, graph, Sum, answer):
    
    if index == len(arr):
        answer[0] = min(answer[0], Sum)
        return
    
    #첫번째 경우
    sx, sy = graph[arr[index]][0][0], graph[arr[index]][0][1]
    lx, ly = graph[arr[index]][1][0], graph[arr[index]][1][1]
    
    k1 = BFS(r,c,sx,sy,test_graph) #첫번째 이모티콘까지 커서 수
    k2 = BFS(sx,sy,lx,ly,test_graph) #두번째 이모티콘까지 커서 수
    
    v1 = test_graph[sx][sy]
    v2 = test_graph[lx][ly]
    test_graph[sx][sy] = 0
    test_graph[lx][ly] = 0
    
    RC(lx,ly,index+1,test_graph,arr,graph, Sum+k1+k2+2, answer)
    
    test_graph[sx][sy] = v1
    test_graph[lx][ly] = v2
    
    
    #두번째 경우
    sx, sy = graph[arr[index]][1][0], graph[arr[index]][1][1]
    lx, ly = graph[arr[index]][0][0], graph[arr[index]][0][1]
    
    k1 = BFS(r,c,sx,sy,test_graph) #첫번째 이모티콘까지 커서 수
    k2 = BFS(sx,sy,lx,ly,test_graph) #두번째 이모티콘까지 커서 수
    
    v1 = test_graph[sx][sy]
    v2 = test_graph[lx][ly]
    test_graph[sx][sy] = 0
    test_graph[lx][ly] = 0
    
    RC(lx,ly,index+1,test_graph,arr,graph, Sum+k1+k2+2, answer)

    test_graph[sx][sy] = v1
    test_graph[lx][ly] = v2
    
    return
    
def solution(board, r, c):
    
    #캐릭터 수 및 위치 초기화
    character = set()
    graph = dict()
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                character.add(board[i][j])
                if board[i][j] not in graph:
                    graph[board[i][j]] = []
                graph[board[i][j]].append([i,j])
    character = list(character)
    
    #삭제할 순서 배열
    arrs = list(itertools.permutations(character))
    
    answer = [int(1e9)]
    
    #순서 배열돌면서 최소 값 확인
    for arr in arrs:
        
        #각 상황을 위한 그래프 초기화
        test_graph = copy.deepcopy(board)
        
        RC(r,c,0,test_graph, arr, graph, 0, answer)
    
    return answer[0]