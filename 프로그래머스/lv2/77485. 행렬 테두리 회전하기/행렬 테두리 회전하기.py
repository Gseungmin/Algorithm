def solution(rows, columns, queries):
    #그래프 초기화
    graph = []
    cnt = 1
    for i in range(rows):
        List = []
        for j in range(columns):
            List.append(cnt)
            cnt += 1
        graph.append(List)

    answer = []

    for querie in queries:
        x1, y1, x2, y2 = querie
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1

        Min = int(1e9)

        new_value = dict()

        #오른쪽 이동 처리
        for i in range(y1,y2):
            new_value[(x1,i+1)] = graph[x1][i]
            Min = min(Min, graph[x1][i])

        #아래로 이동 처리
        for i in range(x1,x2):
            new_value[(i+1,y2)] = graph[i][y2]
            Min = min(Min, graph[i][y2])

        #왼쪽으로 이동 처리
        for i in range(y2,y1,-1):
            new_value[(x2,i-1)] = graph[x2][i]
            Min = min(Min, graph[x2][i])

        #위로 이동 처리
        for i in range(x2,x1,-1):
            new_value[(i-1,y1)] = graph[i][y1]
            Min = min(Min, graph[i][y1])

        #변경사항 그래프에 적용
        for key in new_value:
            x, y = key
            graph[x][y] = new_value[key]

        answer.append(Min)
    return answer