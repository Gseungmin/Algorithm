#양의 수가 더 많아야 함
def RC(now, wolf, sheep, true, info, graph,answer):
    
    if wolf == sheep:
        return
    
    answer[0] = max(answer[0], sheep)
    
    new_now = []
    for i in now:
        check = True
        for j in graph[i]:
            if true[j] == False:
                new_now.append(i)
                break
        
    for i in now:
        for j in graph[i]:
            if true[j] == False:
                if info[j] == 0: #양일 경우
                    true[j] = True
                    new_now.append(j)
                    RC(new_now, wolf, sheep+1, true, info, graph,answer)
                    new_now.pop()
                    true[j] = False
                elif info[j] == 1: #늑대일 경우
                    true[j] = True
                    new_now.append(j)
                    RC(new_now, wolf+1, sheep, true, info, graph,answer)
                    new_now.pop()
                    true[j] = False
    
    return

def solution(info, edges):
    answer = [0]
    
    graph = [[] for i in range(len(info))]
    
    for i, j in edges:
        graph[i].append(j)
    
    wolf = 0
    sheep = 1
    now = [0]
    true = [False]*len(info)
    true[0] = True
    
    RC(now, wolf, sheep, true, info, graph, answer)
    
    return answer[0]