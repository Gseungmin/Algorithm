import sys
input = sys.stdin.readline
import copy
r,c,find = map(int,input().split())
r, c = r-1, c-1
graph = [list(map(int,input().split())) for i in range(3)]

for _ in range(101):
    if r < len(graph) and c < len(graph[0]):
        if graph[r][c] == find:
            print(_)
            sys.exit()
    R = len(graph)
    C = len(graph[0])
    if R >= C:
        new_graph = []
        max_len = 0
        for i in range(R):
            Dict = dict()
            for j in range(C):
                if graph[i][j] == 0:
                    continue
                if graph[i][j] in Dict:
                    Dict[graph[i][j]] += 1
                else:
                    Dict[graph[i][j]] = 1
            List = []
            for j in Dict:
                List.append([Dict[j], j])
            List.sort()
            sorted_list = []
            for x, y in List:
                sorted_list.append(y)
                sorted_list.append(x)
            new_graph.append(sorted_list)
            max_len = max(max_len, len(sorted_list))
        for i in range(len(new_graph)):
            while len(new_graph[i]) < max_len:
                new_graph[i].append(0)
    else:
        new_graph = []
        max_len = 0
        for j in range(C):
            Dict = dict()
            for i in range(R):
                if graph[i][j] == 0:
                    continue
                if graph[i][j] in Dict:
                    Dict[graph[i][j]] += 1
                else:
                    Dict[graph[i][j]] = 1
            List = []
            for k in Dict:
                List.append([Dict[k], k])
            List.sort()
            sorted_list = []
            for x, y in List:
                sorted_list.append(y)
                sorted_list.append(x)
            max_len = max(max_len, len(sorted_list))
            while len(new_graph) < max_len:
                new_graph.append([0]*len(graph[0]))
            for i in range(len(sorted_list)):
                new_graph[i][j] = sorted_list[i]
        max_len = 0
        for i in range(len(new_graph)):
            max_len = max(max_len, len(new_graph[i]))
        for i in range(len(new_graph)):
            while len(new_graph[i]) < max_len:
                new_graph[i].append(0)
    while len(new_graph) > 100:
        new_graph.pop()
    for i in range(len(new_graph)):
        while len(new_graph[i]) > 100:
            new_graph[i].pop()
    graph = copy.deepcopy(new_graph)
print(-1)