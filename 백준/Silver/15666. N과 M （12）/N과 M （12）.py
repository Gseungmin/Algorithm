import sys
input = sys.stdin.readline
N, M = map(int,input().split())
seq = [0] + list(map(int,input().split()))
seq.sort()
true = [0]*9
List = []
ans = []
def pick(N,M,start,true,List,ans):
    if M == 0:
        ans.append(tuple(List))
        return
    for i in range(start,N+1):
        List.append(seq[i])
        pick(N,M-1,i,true,List,ans)
        List.pop()
    return

pick(N,M,1,true,List,ans)
ans = list(set(ans))
ans.sort()
for i in ans :
    print(' '.join(map(str,i)))