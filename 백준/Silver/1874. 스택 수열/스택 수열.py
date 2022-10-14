import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
stack = deque()
answer = []
cnt = 1
for i in range(N):
    value = int(input())
    while cnt <= value:
        stack.append(cnt)
        answer.append('+')
        cnt += 1
    if stack[-1] == value:
        answer.append('-')
        stack.pop()
if stack:
    print('NO')
else:
    print('\n'.join(answer))
