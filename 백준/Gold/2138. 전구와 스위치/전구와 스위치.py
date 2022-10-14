N = int(input())
dx = [-1,0,1]
def flip(graph, x, dx):
    for i in range(3):
        nx = x + dx[i]
        if 0<=nx<N:
            if graph[nx] == 1:
                graph[nx] = 0
            elif graph[nx] == 0:
                graph[nx] = 1
    return
A1 = list(map(int,list(input())))
A2 = []
for i in range(N):
    if i == 0 or i == 1:
        if A1[i] == 0:
            A2.append(1)
        elif A1[i] == 1:
            A2.append(0)
    else:
        A2.append(A1[i])
B = list(map(int,list(input())))
check1 = 0 #0번 인덱스에서 안눌렀다는 조건
for i in range(1,N):
    if A1[i-1] != B[i-1]:
        check1 += 1
        flip(A1, i, dx)
check2 = 1 #0번 인덱스에서 눌렀다는 조건
for i in range(1,N):
    if A2[i-1] != B[i-1]:
        check2 += 1
        flip(A2, i, dx)
if A1 == B:
    print(check1)
    exit()
if A2 == B:
    print(check2)
    exit()
print(-1)