import sys
input = sys.stdin.readline
N, M = map(int,input().split())
seq = [0] + list(map(int,input().split()))
seq.sort()
List = []
def pick_m(N,M,start,List):
    if M == 0: #만약 다 골랐을경우
        for i in List:
            print(i, end = " ")
        print()
        return
    for i in range(start,N+1):
        List.append(seq[i])
        pick_m(N,M-1,i,List)
        List.pop()
    return

pick_m(N,M,1,List)
