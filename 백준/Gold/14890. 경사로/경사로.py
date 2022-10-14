import sys
input = sys.stdin.readline
N, L = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
cnt = 0
for i in range(N):
    Dict = dict()
    check = True
    for j in range(N-1):
        if abs(graph[i][j]-graph[i][j+1]) > 1:
            check = False
            break
        if graph[i][j] != graph[i][j+1]:
            if graph[i][j+1] > graph[i][j]:
                k = graph[i][j]
                if (i,j) in Dict:
                    check = False
                    break
                Dict[(i,j)] = 1
                nj = j-1
                m = 1
                while nj >= 0 and graph[i][nj] == k and (i,nj) not in Dict and m < L:
                    Dict[(i,nj)] = 1
                    nj -= 1
                    m += 1
                if m < L:
                    check = False
                    break
            elif graph[i][j+1] < graph[i][j]:
                k = graph[i][j+1]
                nj = j+1
                m = 0
                while nj < N and graph[i][nj] == k and (i,nj) not in Dict and m < L:
                    Dict[(i,nj)] = 1
                    nj += 1
                    m += 1
                if m < L:
                    check = False
                    break
    if check == True:
        cnt += 1
for j in range(N):
    check = True
    Dict = dict()
    for i in range(N-1):
        if abs(graph[i][j]-graph[i+1][j]) > 1:
            check = False
            break
        if graph[i][j] != graph[i+1][j]:
            if graph[i+1][j] > graph[i][j]:
                k = graph[i][j]
                if (i,j) in Dict:
                    check = False
                    break
                Dict[(i,j)] = 1
                ni = i-1
                m = 1
                while ni >= 0 and graph[ni][j] == k and (ni,j) not in Dict and m < L:
                    Dict[(ni,j)] = 1
                    ni -= 1
                    m += 1
                if m < L:
                    check = False
                    break
            elif graph[i+1][j] < graph[i][j]:
                k = graph[i+1][j]
                ni = i+1
                m = 0
                while ni < N and graph[ni][j] == k and (ni,j) not in Dict and m < L:
                    Dict[(ni,j)] = 1
                    ni += 1
                    m += 1
                if m < L:
                    check = False
                    break
    if check == True:
        cnt += 1
print(cnt)