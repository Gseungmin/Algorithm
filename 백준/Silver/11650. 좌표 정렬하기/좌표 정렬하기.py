import sys
input = sys.stdin.readline
N = int(input())
List = [list(map(int,input().split())) for i in range(N)]
List.sort()
for x, y in List:
    print(x, end = " ")
    print(y)