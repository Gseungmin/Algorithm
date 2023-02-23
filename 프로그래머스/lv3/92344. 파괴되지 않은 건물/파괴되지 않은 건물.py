#2:12
#N*M, 내구도를 각 칸마다 가짐, 적은 파괴, 아군은 회복
#공격 또는 회복이 끝난 후 파괴되지 않은 건물의 개수

#경우의 수가 너무 크기 때문에, 이분탐색, 다익, UF, 누적합 중 하나
#이분탐색 아니고, 다익 아니고, UF아니고 그럼 누적합?
def solution(board, skill):
    
    N, M = len(board), len(board[0])
    
    #누적합 상태를 나타내줄 그래프
    graph = [[0]*(M+1) for i in range(N+1)]
    
    #각 경우 보면서 누적합 적용
    for each in skill:
        type, r1, c1, r2, c2, degree = each
        
        #공격일 경우
        if type == 1:
            graph[r1][c1] += degree
            graph[r1][c2+1] -= degree
            graph[r2+1][c1] -= degree
            graph[r2+1][c2+1] += degree
        else: #회복일 경우
            graph[r1][c1] -= degree
            graph[r1][c2+1] += degree
            graph[r2+1][c1] += degree
            graph[r2+1][c2+1] -= degree
    
    #열 누적합
    for i in range(N):
        for j in range(M):
            graph[i][j+1] += graph[i][j]
    
    #행 누적합
    for j in range(M):
        for i in range(N):
            graph[i+1][j] += graph[i][j]
            
    #prefix 적용
    answer = 0
    for i in range(N):
        for j in range(M):
            board[i][j] -= graph[i][j]
            if board[i][j] > 0:
                answer += 1
    
    return answer