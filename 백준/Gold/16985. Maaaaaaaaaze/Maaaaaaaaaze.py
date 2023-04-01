#3:7
#5*5 크기 판 5개가 주어짐
#하얀 칸만 들어갈 수 있음
#시계 또는 반시계 회전 가능
#판을 쌓는 순서도 제각각 다르고 탈출이 가능해야 함
#가장 적은 이동 횟수 구해라

#1. 4*4*4*4*4*5!의 경우의 수 구하기 = 1024*120
#2. 각 경우마다 이동 가능한 경로 구하기 = 5*5*5 = 125 백트래킹을 통해 시간 단축 가능
#3. 총 경우의 수 1024*120*125

#백트래킹
#1. 기준 값보다 큰경우 return
#2. 입구 또는 출구가 0인 경우 return

import sys
input = sys.stdin.readline
from collections import deque
import copy

Map = [[list(map(int,input().split())) for i in range(5)] for j in range(5)]

#회전 로직
def rotate(graph):
    new_graph = []
    for j in range(5):
        List = []
        for i in range(4,-1,-1):
            List.append(graph[i][j])
        new_graph.append(List)
    return new_graph

dx = [-1,1,0,0]
dy = [0,0,-1,1]
dz = [-1,1]

#최단 경로 구하는 알고리즘
def BFS(A,B,C,D,E,Max):
    true = [[[0]*5 for i in range(5)] for j in range(5)]
    queue = deque()
    all_graph = [A, B, C, D, E]
    queue.append([0,0,0])
    while queue:
        x, y, z = queue.popleft()
        dist = (4-x)+(4-y)+(4-z)
        
        if true[x][y][z] + dist >= Max[0]:
            continue
        
        if true[x][y][z] >= Max[0]:
            return
        
        if z == 4 and x == 4 and y == 4:
            Max[0] = true[x][y][z]
            return
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<5 and 0<=ny<5:
                if all_graph[nx][ny][z] == 1:
                    if true[nx][ny][z] == 0:
                        true[nx][ny][z] = true[x][y][z] + 1
                        queue.append([nx,ny,z])
        for i in range(2):
            nz = z+dz[i]
            if 0<=nz<5:
                if all_graph[x][y][nz] == 1:
                    if true[x][y][nz] == 0:
                        true[x][y][nz] = true[x][y][z] + 1
                        queue.append([x,y,nz])
    return

import itertools
per = list(itertools.permutations(Map)) #모든 블록 경우의 수 구하기

#각 경우마다 check
def check(case, Max):
    
    all_case = [] #i, j는 i 인덱스에서 j형태 그래프를 가짐 가짐
    for i in range(5):
        each = [] #각 인덱스가 가질 케이스
        for j in range(4):
            new_graph = rotate(case[i])
            case[i] = new_graph
            each.append(new_graph)
        all_case.append(each)
    
    for a in range(4): #각 그래프를 골라서
        A = all_case[0][a]
        for b in range(4):
            B = all_case[1][b]
            for c in range(4):
                C = all_case[2][c]
                for d in range(4):
                    D = all_case[3][d]
                    for e in range(4):
                        E = all_case[4][e]
                        if A[0][0] == 0 or E[4][4] == 0: #무조건 실패
                            continue
                        BFS(A,B,C,D,E,Max)
    return


#각 경우의수돌면서 최단거리 찾기
Max = [int(1e9)]
for i in range(len(per)):
    case = per[i]
    per[i] = list(case)
    check(per[i], Max)

if Max[0] == int(1e9):
    print(-1)
else:
    print(Max[0])