import sys
input = sys.stdin.readline
a, b = map(int,input().split())
def p(num):
    return 2*num
def m(num):
    return num*num
from collections import deque
if a == b:
    print(0)
    sys.exit()
elif b == 1:
    print("/")
    sys.exit()
elif b == 0:
    print("-")
    sys.exit()
elif a == 0:
    print(-1)
    sys.exit()
queue = deque()
queue.append([a, ""])
Set = set()
check = 0

Set.add(a)
while queue:
    x, s = queue.popleft()
    if x == b:
        print(s)
        sys.exit()
    P = p(x)
    M = m(x)
    if M <= 1000000000:
        if M not in Set:
            Set.add(M)
            queue.append([M, s+"*"])
    if P <= 1000000000:
        if P not in Set:
            Set.add(P)
            queue.append([P, s+"+"])
    if check == 0:
        queue.append([1, "/"])
        Set.add(1)
        check = 1
print(-1)