import sys
input = sys.stdin.readline

N = int(input())
List = list(map(int,input().split()))

def reculsive(N, index, List, Sum, check):
    if index == N:
        return
    Sum += List[index]
    check.add(Sum)
    reculsive(N, index+1, List, Sum, check)
    Sum -= List[index]
    reculsive(N, index+1, List, Sum, check)
    return

check = set()
reculsive(N, 0, List, 0, check)
i = 1
while 1:
    if i not in check:
        print(i)
        break
    i += 1