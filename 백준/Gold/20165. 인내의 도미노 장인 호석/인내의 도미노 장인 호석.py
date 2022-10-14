def domino(x,y,d):
    if true[x][y] == "F":
        return
    true[x][y] = "F"
    cnt[0] += 1
    for i in range(1,graph[x][y]):
        if d == "E":
            if y+i < M:
                domino(x,y+i,d)
            else:
                break
        if d == "W":
            if y-i >= 0:
                domino(x,y-i,d)
            else:
                break
        if d == "S":
            if x+i < N:
                domino(x+i,y,d)
            else:
                break
        if d == "N":
            if x-i >= 0:
                domino(x-i,y,d)
            else:
                break
    return

N, M, R = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
true = [["S"]*M for i in range(N)]
ans = 0
for i in range(R):
    x, y, d = map(str,input().split(" "))
    x, y = int(x)-1, int(y)-1
    cnt = [0]
    domino(x,y,d)
    ans += cnt[0]
    x, y = map(int,input().split())
    true[x-1][y-1] = "S"
print(ans)
for i in range(N):
    print(" ".join(true[i]))