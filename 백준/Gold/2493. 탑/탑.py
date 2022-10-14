import sys
input = sys.stdin.readline
N = int(input())
List = list(map(int,input().split()))
stack = []
ans = [0]*N
for i in range(N-1,-1,-1):
    while stack and List[stack[-1]] < List[i]:
        ans[stack[-1]] = i+1
        stack.pop()
    stack.append(i)
print(" ".join(map(str,ans)))