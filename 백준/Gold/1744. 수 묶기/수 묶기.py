import sys
input = sys.stdin.readline
p = []
m = []
zero = 0
N = int(input())
for i in range(N):
    a = int(input())
    if a > 0:
        p.append(a)
    elif a < 0:
        m.append(a)
    else:
        zero += 1
p.sort(reverse=True)
m.sort()
total = 0
index = 1
while index < len(p):
    if p[index] == 1 or p[index-1] == 1:
        total += p[index]+p[index-1]
    else:
        total += p[index]*p[index-1]
    index += 2
index = 1
while index < len(m):
    total += m[index]*m[index-1]
    index += 2
if zero == 0 and len(m)%2 == 1:
    total += m[-1]
if len(p)%2 == 1:
    total += p[-1]
print(total)