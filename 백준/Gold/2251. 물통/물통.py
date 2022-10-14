import sys
input = sys.stdin.readline
A, B, C = map(int,input().split())
true = [[-1]*(B+1) for i in range(A+1)]
from collections import deque
queue = deque()
true[0][0] = C
queue.append([0,0])
while queue:
    a, b = queue.popleft()
    c = true[a][b]
    # c->a
    if a+c <= A:
        if true[a+c][b] == -1:
            true[a+c][b] = 0
            queue.append([a+c,b])
    else:
        if true[A][b] == -1:
            true[A][b] = a+c-A
            queue.append([A,b])
    # c->b
    if b+c <= B:
        if true[a][b+c] == -1:
            true[a][b+c] = 0
            queue.append([a,b+c])
    else:
        if true[a][B] == -1:
            true[a][B] = b+c-B
            queue.append([a,B])
    # a->b
    if a+b <= B:
        if true[0][a+b] == -1:
            true[0][a+b] = c
            queue.append([0,a+b])
    else:
        if true[a+b-B][B] == -1:
            true[a+b-B][B] = c
            queue.append([a+b-B,B])
    # a->c
    if a+c <= C:
        if true[0][b] == -1:
            true[0][b] = a+c
            queue.append([0,b])
    else:
        if true[a+c-C][b] == -1:
            true[a+c-C][b] = C
            queue.append([a+c-C,b])
    # b->a
    if b+a <= A:
        if true[b+a][0] == -1:
            true[b+a][0] = c
            queue.append([b+a,0])
    else:
        if true[A][a+b-A] == -1:
            true[A][a+b-A] = c
            queue.append([A,a+b-A])
    # b->c
    if b+c <= C:
        if true[a][0] == -1:
            true[a][0] = b+c
            queue.append([a,0])
    else:
        if true[a][b+c-C] == -1:
            true[a][b+c-C] = C
            queue.append([a,b+c-C])
            
ans = []
for i in range(B+1):
    if true[0][i] != -1:
        ans.append(true[0][i])
ans.sort()
for i in ans:
    print(i, end = " ")