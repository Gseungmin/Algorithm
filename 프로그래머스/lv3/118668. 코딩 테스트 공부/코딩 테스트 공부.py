import heapq

def solution(alp, cop, problems):
    #초기화
    max_al = 0
    max_co = 0
    for i in problems:
        x, y = i[0], i[1]
        max_al = max(x, max_al)
        max_co = max(y, max_co)

    INF = int(1e9)
    true = [[False]*(151) for i in range(151)]
    dist = [[INF]*(151) for i in range(151)]

    dist[alp][cop] = 0
    heap = [[0,alp,cop]]
    while heap:
        k, x, y = heapq.heappop(heap)

        #종료 조건
        if x >= max_al and y >= max_co:
            return k
            break

        if true[x][y] == True:
            continue
        true[x][y] = True

        #알고리즘 공부
        nx, ny = min(x+1, 150), y
        if true[nx][ny] == False:
            if dist[nx][ny] > k+1:
                dist[nx][ny] = k+1
                heapq.heappush(heap,[k+1,nx,ny])

        #코딩 공부
        nx, ny = x, min(y+1, 150)
        if true[nx][ny] == False:
            if dist[nx][ny] > k+1:
                dist[nx][ny] = k+1
                heapq.heappush(heap,[k+1,nx,ny])

        #문제 풀이
        for a, b, c, d, e in problems:
            if a <= x and b <= y:
                nx, ny = min(150, x+c), min(150, y+d)
                if true[nx][ny] == False:
                    if dist[nx][ny] > k+e:
                        dist[nx][ny] = k+e
                        heapq.heappush(heap,[k+e,nx,ny])
    return answer