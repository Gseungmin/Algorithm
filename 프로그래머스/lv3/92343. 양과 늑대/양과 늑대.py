def RC(true, sheep, wolf, info, ans, graph):
    
    #이동할 수 있는 경우
    List = []
    for i in range(len(info)):
        if true[i] == 2:
            for j in graph[i]:
                if true[j] == 0:
                    List.append(j)
    
    if len(List) == 0:
        ans[0] = max(ans[0], sheep)
        return
    
    for i in List:
        if info[i] == 1: #늑대일 경우
            if sheep > wolf+1:
                true[i] = 2
                RC(true, sheep, wolf+1, info, ans, graph)
                true[i] = 0
            else:
                true[i] = 1
                RC(true, sheep, wolf, info, ans, graph)
                true[i] = 0
        
        if info[i] == 0: #양일 경우
            true[i] = 2
            RC(true, sheep+1, wolf, info, ans, graph)
            true[i] = 0
    return

def solution(info, edges):
    answer = 0
    
    #연결상태 초기화
    graph = [[] for i in range(len(info))]
    for i, j in edges:
        graph[i].append(j)
    
    #현재 상태 초기화
    true = [0]*len(info)
    true[0] = 2
    
    ans = [0]
    RC(true, 1, 0, info, ans, graph)
    
    return ans[0]