import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]

from collections import deque

big = []
true = [False]*(N+1)
for i in range(N):
    if true[i] == False:
        small = []
        small.append(i+1)
        
        queue = deque()
        queue.append(i)
        true[i] = True
        while queue:
            x = queue.popleft()
            for nx in range(N):
                if true[nx] == False:
                    if graph[x][nx] == 0: #좋아한다면
                        queue.append(i)
                        true[nx] = True
                        small.append(nx+1)
        
        #종료 조건
        if len(small) == 1:
            print(0)
            sys.exit()
        
        check = True
        for x in range(len(small)):
            for y in range(x+1,len(small)):
                i, j = small[x]-1, small[y]-1
                if graph[i][j] == 1: #같은 집단이지만 서로 싫어하면
                    check = False
                    print(0)
                    sys.exit()
                    break
        
        small.sort()
        
        big.append(small)

print(len(big))
for i in big:
    for j in i:
        print(j, end = " ")
    print()