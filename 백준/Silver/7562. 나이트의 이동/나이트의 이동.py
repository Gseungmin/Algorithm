import sys
input = sys.stdin.readline

def BFS(x, y, dx, dy, true, ans, f_x, f_y):
    queue = []
    true[x][y] = 1 #(x,y)좌표를 방문했다고 표시해준 후
    queue.append([x,y]) #큐에 (x,y)좌료를 넣어준다.
    while queue:
        a, b = queue.pop(0)
        for i in range(8):
            c = a + dx[i]
            d = b + dy[i]
            if (0<=c<N) and (0<=d<N):
                if true[c][d] == 0:
                    true[c][d] = 1
                    queue.append([c,d])
                    ans[c][d] = ans[a][b] + 1
                    if (c==f_x) and (d==f_y):
                        print(ans[c][d])
                        return
    return

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]

T = int(input())
for case in range(T):
    N = int(input())
    ans = []
    true = []
    for i in range(N):
        ans.append([0]*N)
        true.append([0]*N)
    x, y = map(int, input().split())
    f_x, f_y = map(int, input().split())
    if x == f_x and y == f_y:
        print(0)
    else:
        BFS(x, y, dx, dy, true, ans, f_x, f_y)