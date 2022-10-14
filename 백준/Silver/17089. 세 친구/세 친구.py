import sys
input = sys.stdin.readline
N, M = map(int,input().split())
true = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int,input().split())
    true[a].append(b)
    true[b].append(a)

def RC(x, cnt, prev, friends, ans):
    if cnt == 3:
        Sum = 0
        for i in friends:
            Sum += len(true[i])
        if ans[0] == 0:
            ans[1] = Sum-6
            ans[0] = 1
        else:
            ans[1] = min(ans[1], Sum-6)
        return
    for dx in true[x]:
        if dx in friends:
            continue
        if prev != -1:
            if prev not in true[dx]:
                continue
            friends.add(dx)
            RC(dx, cnt+1, x, friends, ans)
            friends.discard(dx)
        else:
            friends.add(dx)
            RC(dx, cnt+1, x, friends, ans)
            friends.discard(dx)
    return
    
ans = [0,-1]
for i in range(1, N+1):
    friends = set()
    friends.add(i)
    RC(i, 1, -1, friends, ans)
    
print(ans[1])