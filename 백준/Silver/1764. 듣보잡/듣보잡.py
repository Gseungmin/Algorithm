N, M = map(int,input().split())
S1 = set()
S2 = set()
for i in range(N):
    S1.add(input())
for j in range(M):
    Str = input()
    if Str in S1:
        S2.add(Str)
ans = list(S2)
ans.sort()
print(len(ans))
for i in ans:
    print(i)