#조세퍼스
import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
queue = deque()
for i in range(1,N+1):
    queue.append(i)
josep = []
while queue:
    for j in range(K):
        if j == K-1:
            josep.append(queue.popleft())
        else:
            queue.append(queue.popleft())
print('<' + ', '.join(map(str,josep)) + '>')