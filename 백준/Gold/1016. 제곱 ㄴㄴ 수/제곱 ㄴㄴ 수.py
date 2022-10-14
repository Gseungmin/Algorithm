import sys
input = sys.stdin.readline
Min, Max = map(int,input().split())
true = [0]*(Max-Min+1)
for i in range(2,1000001):
    if i*i > Max:
        break
    k = i*i
    m = Min%(i*i)
    if m == 0:
        start = Min
    else:
        start = Min+(k-m)
    while start <= Max:
        true[start-Min] = 1
        start += k
ans = 0
for i in range(len(true)):
    if true[i] == 0:
        ans += 1
print(ans)