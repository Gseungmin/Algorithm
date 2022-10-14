import sys
input = sys.stdin.readline
import copy
N = int(input())
Graph = [list(map(int,input().split())) for i in range(N)]
double = [[False]*N for i in range(N)]
ans = [0]

if N == 1:
    print(Graph[0][0])
    sys.exit()

def RC(now, now_d, cnt):
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans[0] = max(ans[0], now[i][j])
        return
    graph1 = copy.deepcopy(now)
    true1 = copy.deepcopy(double)
    for n in range(N):
        i = 0
        j = 1
        while j < N:
            if true1[n][i] == True:
                i += 1
                j = max(j,i+1)
                continue
            if graph1[n][i] == 0:
                if graph1[n][j] != 0:
                    graph1[n][i] = graph1[n][j]
                    graph1[n][j] = 0
                    true1[n][i] = true1[n][j]
                    true1[n][j] = False
                    j += 1
                elif graph1[n][j] == 0:
                    j += 1
            else:
                if graph1[n][j] != 0:
                    if graph1[n][i] == graph1[n][j]:
                        graph1[n][i] *= 2
                        graph1[n][j] = 0
                        true1[n][i] = True
                        true1[n][j] = False
                        i += 1
                        j = max(j,i+1)
                    else:
                        i += 1
                        j = max(j,i+1)
                elif graph1[n][j] == 0:
                    j += 1
    RC(graph1, true1, cnt+1)
    graph2 = copy.deepcopy(now)
    true2 = copy.deepcopy(double)
    for n in range(N):
        i = N-1
        j = N-2
        while j >= 0:
            if true2[n][i] == True:
                i -= 1
                j = min(j,i-1)
                continue
            if graph2[n][i] == 0:
                if graph2[n][j] != 0:
                    graph2[n][i] = graph2[n][j]
                    graph2[n][j] = 0
                    true2[n][i] = true2[n][j]
                    true2[n][j] = False
                    j -= 1
                elif graph2[n][j] == 0:
                    j -= 1
            else:
                if graph2[n][j] != 0:
                    if graph2[n][i] == graph2[n][j]:
                        graph2[n][i] *= 2
                        graph2[n][j] = 0
                        true2[n][i] = True
                        true2[n][j] = False
                        i -= 1
                        j = min(j,i-1)
                    else:
                        i -= 1
                        j = min(j,i-1)
                elif graph2[n][j] == 0:
                    j -= 1
    RC(graph2, true2, cnt+1)
    graph3 = copy.deepcopy(now)
    true3 = copy.deepcopy(double)
    for n in range(N):
        i = 0
        j = 1
        while j < N:
            if true3[i][n] == True:
                i += 1
                j = max(j,i+1)
                continue
            if graph3[i][n] == 0:
                if graph3[j][n] != 0:
                    graph3[i][n] = graph3[j][n]
                    graph3[j][n] = 0
                    true3[i][n] = true3[j][n]
                    true3[j][n] = False
                    j += 1
                elif graph3[j][n] == 0:
                    j += 1
            else:
                if graph3[j][n] != 0:
                    if graph3[i][n] == graph3[j][n]:
                        graph3[i][n] *= 2
                        graph3[j][n] = 0
                        true3[i][n] = True
                        true3[j][n] = False
                        i += 1
                        j = max(j,i+1)
                    else:
                        i += 1
                        j = max(j,i+1)
                elif graph3[j][n] == 0:
                    j += 1
    RC(graph3, true3, cnt+1)
    graph4 = copy.deepcopy(now)
    true4 = copy.deepcopy(double)
    for n in range(N):
        i = N-1
        j = N-2
        while j >= 0:
            if true4[i][n] == True:
                i -= 1
                j = min(j,i-1)
                continue
            if graph4[i][n] == 0:
                if graph4[j][n] != 0:
                    graph4[i][n] = graph4[j][n]
                    graph4[j][n] = 0
                    true4[i][n] = true4[j][n]
                    true4[j][n] = False
                    j -= 1
                elif graph4[j][n] == 0:
                    j -= 1
            else:
                if graph4[j][n] != 0:
                    if graph4[i][n] == graph4[j][n]:
                        graph4[i][n] *= 2
                        graph4[j][n] = 0
                        true4[i][n] = True
                        true4[j][n] = False
                        i -= 1
                        j = min(j,i-1)
                    else:
                        i -= 1
                        j = min(j,i-1)
                elif graph4[j][n] == 0:
                    j -= 1
    RC(graph4, true4, cnt+1)
    return
RC(Graph, double, 0)
print(ans[0])