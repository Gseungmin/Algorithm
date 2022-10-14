import sys
input = sys.stdin.readline
from collections import deque

A, B, C = map(int,input().split())
Sum = A+B+C
if A == B and A == C:
    print(1)
    sys.exit()
elif Sum % 3 != 0:
    print(0)
    sys.exit()

c = [[-1]*1501 for i in range(1501)]

def BFS(A, B, c):
    queue = deque()
    c[A][B] = Sum-A-B
    queue.append([A,B])
    while queue:
        a, b = queue.popleft()
        if a == b and a == c[a][b]:
            print(1)
            sys.exit()
        if a != c[a][b]:
            if a > c[a][b]:
                if c[a-c[a][b]][c[a][b]+c[a][b]] == -1:
                    c[a-c[a][b]][c[a][b]+c[a][b]] = b
                    queue.append([a-c[a][b],c[a][b]+c[a][b]])
            else:
                if c[a+a][c[a][b]-a] == -1:
                    c[a+a][c[a][b]-a] = b
                    queue.append([a+a,c[a][b]-a])
        if b != c[a][b]:
            if b > c[a][b]:
                if c[b-c[a][b]][c[a][b]+c[a][b]] == -1:
                    c[b-c[a][b]][c[a][b]+c[a][b]] = a
                    queue.append([b-c[a][b],c[a][b]+c[a][b]])
            else:
                if c[b+b][c[a][b]-b] == -1:
                    c[b+b][c[a][b]-b] = a
                    queue.append([b+b,c[a][b]-b])
        if a != b:
            if a > b:
                if c[a-b][b+b] == -1:
                    c[a-b][b+b] = c[a][b]
                    queue.append([a-b,b+b])
            else:
                if c[a+a][b-a] == -1:
                    c[a+a][b-a] = c[a][b]
                    queue.append([a+a,b-a])
    return

List = [A, B, C]
check = 0
for i in List:
    for j in List:
        if i != j:
            check = 1
            BFS(i,j,c)
            break
    if check == 1:
        break
print(0)
sys.exit()