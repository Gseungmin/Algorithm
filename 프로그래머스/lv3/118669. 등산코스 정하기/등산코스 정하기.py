#힙 초기화
import heapq
import sys

def solution(n, paths, gates, summits):
    answer = []
    
    heap = []
    
    INF = sys.maxsize
    true = [False]*(n+1)
    dist = [INF]*(n+1)
    
    for i in gates:
        dist[i] = 0
        heapq.heappush(heap, [0, i, i]) #heap x, y, z -> x는 intensity, y는 현재 노드, z는 출발 노드

    #graph 초기화
    gates = set(gates)
    summits = set(summits)

    graph = [[] for i in range(n+1)]

    for i in range(len(paths)):
        x, y, z = paths[i]
        if x in gates and y in gates: #둘다 출입구면 제외
            continue
        if x in summits and y in summits:
            continue
        graph[x].append([y,z])
        graph[y].append([x,z])

    #다익스트라
    while heap:
        intensity, x, start = heapq.heappop(heap)
        if len(answer) > 0:
            if intensity > answer[1]:
                break
        if true[x] == True:
            continue
        true[x] = True
        if x in summits:
            if len(answer) == 0:
                answer = [x, intensity]
            else:
                answer[0] = min(x, answer[0])
            continue
        for nx, k in graph[x]: #nx는 다음 노드, k는 다음 노드까지 거리
            if true[nx] == False:
                if nx in gates: #다른 출입구라면
                    continue
                value = max(intensity, k)
                if dist[nx] > value:
                    dist[nx] = value
                    heapq.heappush(heap, [dist[nx], nx, start])

    return answer