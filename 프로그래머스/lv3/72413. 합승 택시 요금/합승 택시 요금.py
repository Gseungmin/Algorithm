#7:50
#합승을 통해 택시 요금 아끼는 문제
#s에서 모든 경우의 수 구하기
#1.합승해서 어떤 지점에서 내려서 따로가기
#2.처음부터 따로가기
#3.합승해서 가다가 한명이 내린 후 다른 한사람이 그대로 가기

def solution(n, s, a, b, fares):
    INF = int(1e9)
    
    #최단거리 그래프 초기화
    dist = [[int(1e9)]*n for i in range(n)]
    for x,y,k in fares:
        dist[x-1][y-1] = k
        dist[y-1][x-1] = k

    #플로이드 워셜 알고리즘을 통해 최단 거리 초기화
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or i == k or k == j:
                    continue
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    #각자 위치 초기화
    s, a, b = s-1, a-1, b-1
    
    ans = int(1e9)
    #Condition1: 어느지점에서 내린 후 따로가기
    for i in range(n):
        if i != s and i != a and i != b:
            ans = min(ans, dist[s][i]+dist[i][a]+dist[i][b])
    
    #Condition2: 처음부터 따로가기
    ans = min(ans, dist[s][a]+dist[s][b])
    
    #Condition3-1:A가 먼저 내린 후 B가 내리기
    ans = min(ans, dist[s][a]+dist[a][b])
    
    #Condition3-1:B가 먼저 내린 후 A가 내리기
    ans = min(ans, dist[s][b]+dist[b][a])
    
    return ans