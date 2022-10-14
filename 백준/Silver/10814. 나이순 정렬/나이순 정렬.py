import sys
input = sys.stdin.readline
N = int(input())
List = []
k = 0
for i in range(N):
    a, b = map(str,input().split())
    List.append([int(a),k,b])
    k += 1
List.sort()
for i in List:
    print(i[0], end = " ")
    print(i[2])