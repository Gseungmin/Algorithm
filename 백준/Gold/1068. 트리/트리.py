import sys
input = sys.stdin.readline
N = int(input())
parent = list(map(int,input().split()))
tree = [[] for i in range(N)]
for i in range(N):
    if parent[i] == -1:
        root = i
    else:
        tree[parent[i]].append(i)
k = int(input())
if k == root:
    print(0)
    sys.exit()

ans = [0]
def DFS(x):
    check = 0
    for nx in tree[x]:
        if nx == k:
            continue
        check += 1
        DFS(nx)
    if check == 0:
        ans[0] += 1
    return
DFS(root)
print(ans[0])