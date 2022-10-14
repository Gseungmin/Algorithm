import sys
input = sys.stdin.readline
N = int(input())
List = []
for i in range(N):
    A, B = map(int,input().split())
    List.append([B,A])
List.sort()
for i in List:
    print(i[1], end = " ")
    print(i[0])