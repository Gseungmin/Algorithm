import sys
input = sys.stdin.readline
N, K = map(int,input().split())

from collections import deque
true = [-1]*100001
def BFS(N, K, true):
    queue1 = deque()
    queue2 = deque()
    queue1.append(N)
    true[N] = 0
    while 1:
        while queue1:
            x = queue1.popleft()
            if 2*x <= 100000:
                if true[2*x] == -1:
                    true[2*x] = true[x]
                    queue1.append(2*x)
            if x+1 <= 100000:
                if true[x+1] == -1:
                    true[x+1] = true[x] + 1
                    queue2.append(x+1)
            if 0 <= x-1:
                if true[x-1] == -1:
                    true[x-1] = true[x] + 1
                    queue2.append(x-1)
            if true[K] != -1:
                print(true[K])
                sys.exit()
        queue1, queue2 = queue2, queue1
    return

BFS(N, K, true)