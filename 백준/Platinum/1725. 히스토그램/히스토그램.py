import sys
input = sys.stdin.readline
N = int(input())
List = [int(input()) for i in range(N)]
stack = []
Max = 0
for i in range(N):
    while stack and List[stack[-1]] > List[i]:
        H_i = stack.pop()
        W = i
        H = List[H_i]
        if stack:
            W = i-stack[-1]-1
        Max = max(Max, W*H)
    stack.append(i)
while stack:
    H_i = stack.pop()
    W = N
    H = List[H_i]
    if stack:
        W = N-stack[-1]-1 
    Max = max(Max, W*H)
print(Max)