import sys
input = sys.stdin.readline
N, K = map(int,input().split())

from collections import deque
true = [-1]*100001
def BFS(N, K, true):
    queue = deque()
    queue.append(N)
    true[N] = 0
    while queue:
        x = queue.popleft()
        if x+1 <= 100000:
            if true[x+1] == -1:
                true[x+1] = true[x] + 1
                queue.append(x+1)
        if 0 <= x-1:
            if true[x-1] == -1:
                true[x-1] = true[x] + 1
                queue.append(x-1)
        if 2*x <= 100000:
            if true[2*x] == -1:
                true[2*x] = true[x] + 1
                queue.append(2*x)
        if true[K] != -1:
            print(true[K])
            sys.exit()
    return

BFS(N, K, true)