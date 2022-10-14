import sys
input = sys.stdin.readline
N, M = map(int,input().split())
seq = [0] + list(map(int,input().split()))
seq.sort()
true = [0]*9
List = []
ans = []
def pick(N,M,true,List,ans):
    if M == 0:
        ans.append(tuple(List))
        return
    for i in range(1,N+1):
        if true[i] == 0:
            List.append(seq[i])
            true[i] = 1
            pick(N,M-1,true,List,ans)
            true[i] = 0
            List.pop()
    return

pick(N,M,true,List,ans)
ans = list(set(ans))
ans.sort()
for i in ans :
    print(' '.join(map(str,i)))