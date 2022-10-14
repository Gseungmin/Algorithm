import sys
input = sys.stdin.readline
N = int(input())
seq = list(map(int,input().split()))
Set = set()
for i in seq:
    Set.add(i)

ans = []
def RC(N, Set, ans):
    if len(ans) == N:
        print(" ".join(map(str,ans)))
        sys.exit()
    if ans[-1]*2 in Set:
        k = ans[-1]*2
        ans.append(k)
        Set.discard(k)
        RC(N, Set, ans)
        Set.add(k)
        ans.pop()
    if ans[-1]%3 == 0:
        if ans[-1]//3 in Set:
            k = ans[-1]//3
            ans.append(k)
            Set.discard(k)
            RC(N, Set, ans)
            Set.add(k)
            ans.pop()
    return

for i in seq:
    ans.append(i)
    Set.discard(i)
    RC(N, Set, ans)
    Set.add(i)
    ans.pop()