import sys
input = sys.stdin.readline
N, M = map(int,input().split())
List = list(map(int,input().split()))
Sum = sum(List[:M])
left = 0
right = M
ans = Sum
while right < N:
    Sum -= List[left]
    Sum += List[right]
    left, right = left+1, right+1
    ans = max(ans, Sum)
print(ans)