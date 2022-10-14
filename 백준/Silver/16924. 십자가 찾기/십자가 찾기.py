N, M = map(int,input().split())
graph = [list(input()) for i in range(N)]
true = [[0]*M for i in range(N)]
ans = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == '.':
            continue
        cnt = 0
        k = 1
        while 1:
            check = 0
            if i+k < N and i-k >= 0 and j+k < M and j-k >= 0:
                if graph[i+k][j] == '*':
                    if graph[i-k][j] == '*':
                        if graph[i][j+k] == '*':
                            if graph[i][j-k] == '*':
                                cnt += 1
                                true[i+k][j] = 1
                                true[i-k][j] = 1
                                true[i][j+k] = 1
                                true[i][j-k] = 1
                                true[i][j] = 1
                                ans.append([i+1,j+1,cnt])
                                check = 1
            if check == 0:
                break
            k += 1
for i in range(N):
    for j in range(M):
        if graph[i][j] == ".":
            if true[i][j] == 1:
                print(-1)
                exit()
        if graph[i][j] == "*":
            if true[i][j] == 0:
                print(-1)
                exit()
print(len(ans))
for i in ans:
    for j in i:
        print(j, end = " ")
    print()