import sys
input = sys.stdin.readline
N, K = map(int,input().split())
List = list(map(int,input().split()))

if K == N:
    print(0)
    sys.exit()
elif K == 1:
    print(List[-1]-List[0])
    sys.exit()

dif = []
for i in range(len(List)-1):
    dif.append([List[i+1]-List[i], i, i+1])
dif.sort(reverse = True)

dif = dif[:K-1]
Dict = dict()
for k, i, j in dif:
    Dict[(i,j)] = k

ans = 0

prev = 0
for i in range(N):
    if (i,i+1) in Dict:
        ans += List[i]-List[prev]
        prev = i+1
ans += List[N-1]-List[prev]
print(ans)