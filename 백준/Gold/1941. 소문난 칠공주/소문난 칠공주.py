graph = [list(input()) for i in range(5)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
List = []
ans = [0]
from collections import deque

def RC(index, Y, S, List):
    if Y >= 4:
        return
    if Y+S == 7 and S >= 4:
        check = 0
        queue = deque()
        x, y = List[0][0], List[0][1]
        queue.append([x,y])
        true = set()
        true.add((x,y))
        while queue:
            x, y = queue.popleft()
            check += 1
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if (nx,ny) not in true and [nx,ny] in List:
                    true.add((nx,ny))
                    queue.append([nx,ny])
        if check == 7:
            ans[0] += 1
        return
    if Y+S == 7 or index == 25:
        return
    x, y = index//5, index%5
    List.append([x,y])
    if graph[x][y] == "Y":
        RC(index+1, Y+1, S, List)
    else:
        RC(index+1, Y, S+1, List)
    List.pop()
    RC(index+1, Y, S, List)
    return
RC(0,0,0,List)
print(ans[0])