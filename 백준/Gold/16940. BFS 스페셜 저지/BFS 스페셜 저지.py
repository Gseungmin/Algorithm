import sys
input = sys.stdin.readline
N = int(input())
graph = [set() for i in range(N+1)]
cnt = [0]*(N+1)
for i in range(N-1):
    a, b = map(int,input().split())
    cnt[a] += 1
    cnt[b] += 1
    graph[a].add(b)
    graph[b].add(a)
arr = list(map(int,input().split()))
if arr[0] != 1:
    print(0)
    sys.exit()

from collections import deque
queue = deque()
true = [-1]*(N+1)
true[1] = 0
queue.append(1)
index = 1
while queue:
    x = queue.popleft()
    k = cnt[x]
    while k > 0:
        if arr[index] in graph[x]:
            if true[arr[index]] == -1:
                true[arr[index]] = 0
                queue.append(arr[index])
                cnt[x] -= 1
                cnt[arr[index]] -= 1
                index += 1
                k -= 1
                if index == N:
                    break
        else:
            print(0)
            sys.exit()
    if k != 0:
        print(0)
        sys.exit()
    if index == N:
        break
for i in range(1,N+1):
    if true[i] == -1:
        print(0)
        sys.exit()
print(1)