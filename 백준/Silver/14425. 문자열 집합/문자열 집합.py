N, M = map(int,input().split())
Set = set()
for i in range(N):
    Set.add(input())
ans = 0
for i in range(M):
    s = input()
    if s in Set:
        ans += 1
print(ans)