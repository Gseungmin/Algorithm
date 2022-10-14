import sys
input = sys.stdin.readline
N, M = map(int,input().split())
seq = [0] + list(map(int,input().split()))
seq.sort()
true = [0]*9
List = []
def pick_m(N,M,List):
    if M == 0: #만약 다 골랐을경우
        for i in List:
            print(i, end = " ")
        print()
        return
    for i in range(1,N+1):
        if true[i] == 0:
            true[i] = 1
            List.append(seq[i])
            pick_m(N,M-1,List)
            true[i] = 0
            List.pop()
    return

pick_m(N,M,List)