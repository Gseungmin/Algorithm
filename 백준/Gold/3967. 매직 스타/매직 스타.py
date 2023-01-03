import sys
input = sys.stdin.readline
graph = [list(input().rstrip()) for i in range(5)]
first = [[0,4],[1,3],[2,2],[3,1]]
second = [[3,1],[3,3],[3,5],[3,7]]
third = [[0,4],[1,5],[2,6],[3,7]]
four = [[4,4],[3,5],[2,6],[1,7]]
five = [[1,1],[1,3],[1,5],[1,7]]
six = [[1,1],[2,2],[3,3],[4,4]]

All = [[2,2],[3,1],[3,3],[3,5],[3,7],[0,4],[1,5],[4,4],[2,6],[1,7],[1,1],[1,3]]
All.sort()
Set = set()
for i in range(len(All)-1, -1,-1):
    x, y = All[i]
    if graph[x][y] != "x":
        All.remove([x,y])
        Set.add(graph[x][y])

alpha = []
for i in range(65,77):
    alpha.append(chr(i))

def Sum():
    k1 = 0
    cnt = 0
    for i, j in first:
        if graph[i][j] != "x":
            cnt += 1
            k1 += (ord(graph[i][j])-64)
            if k1 > 26: 
                return 2
            if cnt == 4 and k1 < 26:
                return 2
    
    k2 = 0
    cnt = 0
    for i, j in second:
        if graph[i][j] != "x":
            cnt += 1
            k2 += (ord(graph[i][j])-64)
            if k2 > 26: 
                return 2
            if cnt == 4 and k2 < 26:
                return 2
    
    k3 = 0
    cnt = 0
    for i, j in third:
        if graph[i][j] != "x":
            cnt += 1
            k3 += (ord(graph[i][j])-64)
            if k3 > 26: 
                return 2
            if cnt == 4 and k3 < 26:
                return 2
                
    k4 = 0
    cnt = 0
    for i, j in four:
        if graph[i][j] != "x":
            cnt += 1
            k4 += (ord(graph[i][j])-64)
            if k4 > 26: 
                return 2
            if cnt == 4 and k4 < 26:
                return 2
                
    k5 = 0
    cnt = 0
    for i, j in five:
        if graph[i][j] != "x":
            cnt += 1
            k5 += (ord(graph[i][j])-64)
            if k5 > 26: 
                return 2
            if cnt == 4 and k5 < 26:
                return 2
                
    k6 = 0
    cnt = 0
    for i, j in six:
        if graph[i][j] != "x":
            cnt += 1
            k6 += (ord(graph[i][j])-64)
            if k6 > 26: 
                return 2
            if cnt == 4 and k6 < 26:
                return 2
    
    if k1 == 26 and k2 == 26 and k3 == 26 and k4 == 26 and k5 == 26 and k6 == 26:
        return 1
    
    return 0


def RC(index, All, alpha):
    if Sum() == 2:
        return
    if Sum() == 1:
        for i in graph:
            print("".join(i))
        sys.exit()
    if index == len(All):
        return
    for i in alpha:
        if i in Set:
            continue
        x, y = All[index]
        k = graph[x][y]
        graph[x][y] = i
        Set.add(i)
        RC(index+1, All, alpha)
        Set.remove(i)
        graph[x][y] = k
    return
    
RC(0, All, alpha)