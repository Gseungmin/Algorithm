import sys
input = sys.stdin.readline
N = int(input())
List = list(map(int,input().split()))
from collections import deque
if N == 3:
    HP = [[[-1]*(List[0]+1) for i in range(List[1]+1)] for j in range(List[2]+1)]
    HP[List[2]][List[1]][List[0]] = 0
    queue = deque()
    queue.append([List[2],List[1],List[0]])
    while queue:
        x,y,z = queue.popleft()
        if HP[max(x-9,0)][max(y-3,0)][max(z-1,0)] == -1:
            HP[max(x-9,0)][max(y-3,0)][max(z-1,0)] = HP[x][y][z] + 1
            queue.append([max(x-9,0),max(y-3,0),max(z-1,0)])
        if HP[max(x-9,0)][max(y-1,0)][max(z-3,0)] == -1:
            HP[max(x-9,0)][max(y-1,0)][max(z-3,0)] = HP[x][y][z] + 1
            queue.append([max(x-9,0),max(y-1,0),max(z-3,0)])
        if HP[max(x-3,0)][max(y-9,0)][max(z-1,0)] == -1:
            HP[max(x-3,0)][max(y-9,0)][max(z-1,0)] = HP[x][y][z] + 1
            queue.append([max(x-3,0),max(y-9,0),max(z-1,0)])
        if HP[max(x-3,0)][max(y-1,0)][max(z-9,0)] == -1:
            HP[max(x-3,0)][max(y-1,0)][max(z-9,0)] = HP[x][y][z] + 1
            queue.append([max(x-3,0),max(y-1,0),max(z-9,0)])
        if HP[max(x-1,0)][max(y-3,0)][max(z-9,0)] == -1:
            HP[max(x-1,0)][max(y-3,0)][max(z-9,0)] = HP[x][y][z] + 1
            queue.append([max(x-1,0),max(y-3,0),max(z-9,0)])
        if HP[max(x-1,0)][max(y-9,0)][max(z-3,0)] == -1:
            HP[max(x-1,0)][max(y-9,0)][max(z-3,0)] = HP[x][y][z] + 1
            queue.append([max(x-1,0),max(y-9,0),max(z-3,0)])
        if HP[0][0][0] != -1:
            print(HP[0][0][0])
            sys.exit()
elif N == 2:
    HP = [[-1]*(List[0]+1) for i in range(List[1]+1)]
    HP[List[1]][List[0]] = 0
    queue = deque()
    queue.append([List[1],List[0]])
    while queue:
        x,y = queue.popleft()
        if HP[max(x-9,0)][max(y-3,0)] == -1:
            HP[max(x-9,0)][max(y-3,0)] = HP[x][y] + 1
            queue.append([max(x-9,0),max(y-3,0)])
        if HP[max(x-3,0)][max(y-9,0)] == -1:
            HP[max(x-3,0)][max(y-9,0)] = HP[x][y] + 1
            queue.append([max(x-3,0),max(y-9,0)])
        if HP[0][0] != -1:
            print(HP[0][0])
            sys.exit()
else:
    if List[0]%9 == 0:
        print((List[0]//9))
    else:
        print((List[0]//9)+1)
    sys.exit()