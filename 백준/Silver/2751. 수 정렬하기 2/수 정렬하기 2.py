import sys
input = sys.stdin.readline
N = int(input())
List = [int(input()) for i in range(N)]
List.sort()
for i in List:
    print(i)