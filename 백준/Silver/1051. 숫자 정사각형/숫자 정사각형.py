N, M = map(int,input().split())
List = [list(input()) for i in range(N)]
K = min(N, M)
size = 2
ans = 1
while size <= K:
    for i in range(N-size+1):
        for j in range(M-size+1):
            if List[i][j] == List[i][j+size-1] and List[i][j] == List[i+size-1][j] and List[i][j] == List[i+size-1][j+size-1]:
                ans = size**2
    size += 1
print(ans)