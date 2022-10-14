import sys
input = sys.stdin.readline
N, M, H = map(int,input().split())
graph = [[0]*(N) for i in range(H)]
for i in range(M):
    a, b = map(int,input().split())
    graph[a-1][b-1] = 1
if M == 0:
    print(0)
    sys.exit()
    
List = []
ans = [0,-1]
def RC(index, graph, N, M, H, List, ans):
    if len(List) == 3 or index == N*H:
        check = 0
        for i in range(N):
            k = i
            j = 0
            while j < H:
                if graph[j][k] == 1:
                    k += 1
                elif k >= 1:
                    if graph[j][k-1] == 1:
                        k -= 1
                j += 1
            if i != k:
                check = 1
                break
        if check == 0:
            if ans[0] == 0:
                ans[1] = len(List)
                ans[0] = -1
            else:
                ans[1] = min(ans[1], len(List))
        return
    x, y = (index//N), (index%N)
    if y == N-1:
        RC(index+1, graph, N, M, H, List, ans)
    elif y == 0:
        if graph[x][y] == 0 and graph[x][y+1] == 0:
            List.append([x,y])
            graph[x][y] = 1
            RC(index+1, graph, N, M, H, List, ans)
            List.pop()
            graph[x][y] = 0
        RC(index+1, graph, N, M, H, List, ans)
    else:
        if graph[x][y] == 0 and graph[x][y-1] == 0 and graph[x][y+1] == 0:
            graph[x][y] = 1
            List.append([x,y])
            RC(index+1, graph, N, M, H, List, ans)
            graph[x][y] = 0
            List.pop()
        RC(index+1, graph, N, M, H, List, ans)
    return

RC(0, graph, N, M, H, List, ans)
print(ans[1])