import sys
input = sys.stdin.readline

M, N = map(int,input().split())

#그래프 초기화
graph = [[1]*M for i in range(M)]

for _ in range(N):
    #매일 입력으로 받는 정해진 성장 크기
    Nums = list(map(int,input().split()))
    List = [0]*Nums[0] + [1]*Nums[1] + [2]*Nums[2]
    
    #성장 그래프 초기화
    grow_graph = [[0]*M for i in range(M)]
    
    #입력으로 받은 값 성장 그래프에 바인딩
    for i in range(M):
        grow_graph[M-i-1][0] = List[i]
    for i in range(M,len(List)):
        grow_graph[0][i-M+1] = List[i]
    
    #입력 제외 위치 값 성장 그래프에 바인딩
    index = 1 #x
    while index < M:
        for i in range(index,M): #y
            if i == index:
                for j in range(index,M):
                    grow_graph[j][i] = max(grow_graph[j-1][i], grow_graph[j][i-1], grow_graph[j-1][i-1])
            else:
                grow_graph[index][i] = max(grow_graph[index-1][i], grow_graph[index][i-1], grow_graph[index-1][i-1])
        index += 1
    
    for i in range(M):
        for j in range(M):
            graph[i][j] += grow_graph[i][j]
    
for i in range(M):
    for j in range(M):
        print(graph[i][j], end = " ")
    print()