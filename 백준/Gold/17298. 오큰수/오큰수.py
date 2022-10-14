import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
stack = []
check = [-1]*N
for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        check[stack[-1]] = A[i]
        stack.pop()
    stack.append(i)
print(" ".join(map(str,check)))