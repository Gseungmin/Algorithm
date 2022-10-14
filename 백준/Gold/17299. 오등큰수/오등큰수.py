import sys
input = sys.stdin.readline
A = int(input())
List = list(map(int,input().split()))
Max = max(List)
cnt = [0]*(Max+1)
for i in List:
    cnt[i] += 1
answer = [-1]*A
from collections import deque
stack = deque()
stack.append(0)
for i in range(1,A):
    while cnt[List[i]] > cnt[List[stack[-1]]]:
        answer[stack.pop()] = List[i]
        if not stack:
            break
    stack.append(i)
for i in answer:
    print(i, end = " ")