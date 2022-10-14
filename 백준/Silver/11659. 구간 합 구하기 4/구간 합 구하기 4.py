import sys
input = sys.stdin.readline
N, M = map(int,input().split())
Sum = [0]*N
List = list(map(int,input().split()))
value = 0
for i in range(N):
    value += List[i]
    Sum[i] = value
for i in range(M):
    a, b = map(int,input().split())
    print(Sum[b-1]-Sum[a-1]+List[a-1])