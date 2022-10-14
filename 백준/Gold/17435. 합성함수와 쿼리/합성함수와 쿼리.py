import sys
input = sys.stdin.readline
M = int(input())
List = [0] + list(map(int,input().split()))
Length = 20
parent = [[0]*Length for i in range(M+1)]
for i in range(1,len(List)):
    parent[i][0] = List[i]
for j in range(1,Length):
    for i in range(1,M+1):
        if parent[i][j-1] != 0:
            parent[i][j] = parent[parent[i][j-1]][j-1]
Q = int(input())
for _ in range(Q):
    m, x = map(int,input().split())
    for i in range(Length):
        if (m & (1<<i)) > 0:
            x = parent[x][i]
    print(x)