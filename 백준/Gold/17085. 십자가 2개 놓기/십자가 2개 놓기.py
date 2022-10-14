N, M = map(int,input().split())
graph = [list(input()) for i in range(N)]

find = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == "#":
            s = 1
            while 1:
                if i-s>=0 and i+s<N and j-s>=0 and j+s<M:
                    if graph[i-s][j] == "#" and graph[i+s][j] == "#" and graph[i][j-s] == "#" and graph[i][j+s] == "#":
                        find.append([i,j,s])
                        s += 1
                    else:
                        break
                else:
                    break

Max = [0]
List = []
def RC(index, find, List, Max):
    if len(List) > 2:
        return
    if index == len(find):
        if len(List) == 0:
            Max[0] = max(Max[0], 1)
            return
        Set = set()
        for x, y, s in List:
            while s >= 0:
                if (x+s,y) in Set or (x-s,y) in Set or (x,y+s) in Set or (x,y-s) in Set:
                    return
                Set.add((x+s,y))
                Set.add((x-s,y))
                Set.add((x,y+s))
                Set.add((x,y-s))
                s -= 1
        if len(List) == 1:
            Max[0] = max(Max[0], List[0][2]*4+1)
        else:
            mul = 1
            for i in List:
                mul *= (i[2]*4)+1
            Max[0] = max(Max[0], mul)
        return
    List.append(find[index])
    RC(index+1, find, List, Max)
    List.pop()
    RC(index+1, find, List, Max)
    return

RC(0, find, List, Max)
print(Max[0])