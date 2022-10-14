import sys
input = sys.stdin.readline
N, M = map(int,input().split())

def reculsive(N, M, List):
    if M == 0:
        for i in List:
            print(i, end = " ")
        print()
        return
    for i in range(1, N+1):
        List.append(i)
        reculsive(N, M-1, List)
        List.pop()
    return

List = []
reculsive(N, M, List)