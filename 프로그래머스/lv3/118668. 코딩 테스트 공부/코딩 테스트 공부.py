#알고력과 코딩력
#공부는 알고력과 코딩력을 각각 1씩 높임
#같은 문제 여러번 푸는 것 가능, 각 문제를 풀면 올라가는 알고력과 코딩력이 정해져있음
#모든 문제를 풀 수 있는 알고력과 코딩력을 얻는 최단 시간을 구하려함

import heapq

def solution(alp, cop, problems):
    answer = 0
    
    #힙 초기화
    heap = []
    heapq.heappush(heap, [0,alp,cop])
    INF = int(1e9)
    dist = [[INF]*151 for i in range(151)]
    true = [[False]*151 for i in range(151)]
    dist[alp][cop] = 0

    while heap:
        k, x, y = heapq.heappop(heap)
        
        if true[x][y] == True:
            continue
        
        true[x][y] = True
        check = True
        
        #문제를 풀 수 있다면 풀기
        for a, b, c, d, e in problems:
            nx = min(x+c,150)
            ny = min(y+d,150)
            
            if a <= x and b <= y:
                if true[nx][ny] == False:
                    if dist[nx][ny] > k+e:
                        heapq.heappush(heap, [k+e, nx, ny])
            else:
                check = False
        
        #모든 문제를 풀 수 있다면
        if check == True:
            answer = k
            break
        
        nx = min(x+1,150)
        if true[nx][y] == False:
            if dist[nx][y] > k+1:
                heapq.heappush(heap, [k+1, nx, y])
        
        ny = min(y+1,150)
        if true[x][ny] == False:
            if dist[x][ny] > k+1:
                heapq.heappush(heap, [k+1, x, ny])
    
    return answer