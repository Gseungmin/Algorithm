import sys
input = sys.stdin.readline
N, K = map(int,input().split())
combi = [[1]]
i = 1
while i <= N:
    combi.append([])
    for j in range(i+1):
        if j == 0:
            combi[-1].append(1)
        elif j == i:
            combi[-1].append(1)
        else:
            combi[-1].append((combi[-2][j-1]+combi[-2][j])%10007)
    i += 1
print(combi[N][K]%10007)