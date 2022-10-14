import sys
input = sys.stdin.readline
from collections import deque
t = int(input())
for i in range(t):
    N = int(input())
    true = [-1]*(N)
    queue = deque()
    k = 1%N
    true[k] = 1
    queue.append(k)
    Dict = dict()
    Dict[k] = "1"
    while queue:
        k = queue.popleft()
        if k == 0:
            print(Dict[k])
            break
        if true[k] == 100:
            continue
        n1 = k*10
        if true[n1%N] == -1:
            true[n1%N] = true[k] + 1
            Dict[n1%N] = Dict[k] + "0"
            queue.append(n1%N)
        n2 = k*10+1
        if true[n2%N] == -1:
            true[n2%N] = true[k] + 1
            Dict[n2%N] = Dict[k] + "1"
            queue.append(n2%N)
    if 0 not in Dict:
        print("BRAK")