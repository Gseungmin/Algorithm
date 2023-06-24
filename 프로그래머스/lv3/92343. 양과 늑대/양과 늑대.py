#양과 늑대가 놓여 있음
#양이 더 많아야 함
#최대한 많은 수의 양을 모아 루트 노드로 돌아와야 함
#0은 양, 1은 늑대, 0번 노드에서 시작

#sheep: 양의수, wolf: 늑대수, nodes: 현재 선택된 노드들, graph: 노드 그래프
def RC(sheep, wolf, nodes, graph, ans, info):
    
    if sheep <= wolf:
        return
    
    ans[0] = max(ans[0], sheep)
    
    for x in nodes:
        for nx in graph[x]:
            if nx not in nodes:
                nodes.add(nx)
                if info[nx] == 0:
                    RC(sheep+1, wolf, nodes, graph, ans, info)
                else:
                    RC(sheep, wolf+1, nodes, graph, ans, info)
                nodes.discard(nx)
    
    return

#cond 초기화 및 RC를 통해 문제 해결
def solution(info, edges):
    graph = [[] for i in range(len(info))]
    
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
        
    nodes = set()
    nodes.add(0)
    
    ans = [1]
    RC(1,0,nodes, graph, ans, info)
    
    return ans[0]