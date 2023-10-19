#1:2
#알고력과 코딩력 > 0
#문제에 필요한 알고력과 코딩력이 필요
#알고리즘 및 코딩 공부 각각 1씩 증가, 각 문제마다 풀수록 올라가는 알고력 코딩력 존재
#같은 문제를 여러번 풀어도 무방, 모든 문제를 다 풀 필요는 없음
#모든 문제를 풀 수 있는 알고력과 코딩력을 얻는 최단시간

#Len(problems) = 6

#현재 상황에서 공부하는 2가지 방법 + problems
#problems = [req_a, req_c, a, c]

import heapq
INF = int(1e9)
Limit = 150

def solution(alp, cop, problems):
    answer = 0
    
    true = [[False]*(Limit+1) for i in range(Limit+1)]
    dist = [[INF]*(Limit+1) for i in range(Limit+1)]
    heap = []
    
    heapq.heappush(heap,[0,alp,cop])
    dist[alp][cop] = 0

    while heap:
        t, x, y = heapq.heappop(heap)
        if true[x][y] == True:
            continue
        true[x][y] = True
        
        #알고리즘 공부
        if true[min(x+1, Limit)][y] == False:
            if dist[min(x+1, Limit)][y] > t+1:
                dist[min(x+1, Limit)][y] = t+1
                heapq.heappush(heap, [t+1, min(x+1, Limit), y])
        
        #코딩 공부
        if true[x][min(y+1, Limit)] == False:
            if dist[x][min(y+1, Limit)] > t+1:
                dist[x][min(y+1, Limit)] = t+1
                heapq.heappush(heap, [t+1, x, min(y+1, Limit)])
        
        count = 0
        #문제 풀이
        for i in range(len(problems)):
            req_x, req_y, get_x, get_y, cost = problems[i]
            if req_x <= x and req_y <= y:
                count = count+1
                if true[min(x+get_x, Limit)][min(y+get_y, Limit)] == False:
                    if dist[min(x+get_x, Limit)][min(y+get_y, Limit)] > t+cost:
                        dist[min(x+get_x, Limit)][min(y+get_y, Limit)] = t+cost
                        heapq.heappush(heap, [t+cost, min(x+get_x, Limit), min(y+get_y, Limit)])
        
        if count == len(problems):
            return t
            
    return answer