import sys
input = sys.stdin.readline
N, M = map(int,input().split())
List = list(map(int,input().split()))
Sum = sum(List[:M])
Max = Sum
for i in range(M,N):
    Sum += List[i]
    Sum -= List[i-M]
    Max = max(Max, Sum)
print(Max)