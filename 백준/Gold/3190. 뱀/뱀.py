N = int(input())
K = int(input())
Dict = dict()
for i in range(K):
    a, b = map(int,input().split())
    Dict[(a,b)] = 1
L = int(input())
move = [list(map(str,input().split())) for i in range(L)]
move.append([10001,"D"])
from collections import deque
queue = deque()
queue.append([1,1,1,1,0])
ans = 0
snake = deque()
snake.append([1,1])
index = 0
while queue:
    if index == L+1:
        print(ans)
        break
    i, j = move[index]
    i = int(i)
    i -= ans
    hx, hy, tx, ty, t = queue.popleft()
    nhx, nhy, ntx, nty = hx, hy, tx, ty
    for k in range(i):
        ans += 1
        if t == 0:
            nhy += 1
            if [nhx,nhy] in snake or nhy == N+1:
                print(ans)
                exit()
            if (nhx,nhy) in Dict and Dict[(nhx,nhy)] == 1:
                Dict[(nhx,nhy)] = 0
            else:
                snake.pop()
            snake.appendleft([nhx,nhy])
        if t == 1:
            nhy -= 1
            if [nhx,nhy] in snake or nhy == 0:
                print(ans)
                exit()
            if (nhx,nhy) in Dict and Dict[(nhx,nhy)] == 1:
                Dict[(nhx,nhy)] = 0
            else:
                snake.pop()
            snake.appendleft([nhx,nhy])
        if t == 2:
            nhx += 1
            if [nhx,nhy] in snake or nhx == N+1:
                print(ans)
                exit()
            if (nhx,nhy) in Dict and Dict[(nhx,nhy)] == 1:
                Dict[(nhx,nhy)] = 0
            else:
                snake.pop()
            snake.appendleft([nhx,nhy])
        if t == 3:
            nhx -= 1
            if [nhx,nhy] in snake or nhx == 0:
                print(ans)
                exit()
            if (nhx,nhy) in Dict and Dict[(nhx,nhy)] == 1:
                Dict[(nhx,nhy)] = 0
            else:
                snake.pop()
            snake.appendleft([nhx,nhy])
    nhx, nhy, ntx, nty = snake[0][0], snake[0][1], snake[-1][0], snake[-1][1]
    if t == 0 and j == "D":
        queue.append([nhx,nhy,ntx,nty,2])
    if t == 0 and j == "L":
        queue.append([nhx,nhy,ntx,nty,3])
    if t == 1 and j == "D":
        queue.append([nhx,nhy,ntx,nty,3])
    if t == 1 and j == "L":
        queue.append([nhx,nhy,ntx,nty,2])
    if t == 2 and j == "D":
        queue.append([nhx,nhy,ntx,nty,1])
    if t == 2 and j == "L":
        queue.append([nhx,nhy,ntx,nty,0])
    if t == 3 and j == "D":
        queue.append([nhx,nhy,ntx,nty,0])
    if t == 3 and j == "L":
        queue.append([nhx,nhy,ntx,nty,1])
    index += 1