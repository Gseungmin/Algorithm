import sys
input = sys.stdin.readline
N = int(input())
A, B = map(int,input().split())
a = [int(input()) for i in range(A)]
b = [int(input()) for i in range(B)]
Sum_a = sum(a)
Sum_b = sum(b)
for i in range(A-1):
    a.append(a[i])
for i in range(B-1):
    b.append(b[i])
Dict_a = dict()
Dict_b = dict()
for i in range(A):
    k = 0
    for j in range(i,i+A-1):
        k += a[j]
        if k > N:
            break
        if k not in Dict_a:
            Dict_a[k] = 1
        else:
            Dict_a[k] += 1
for i in range(B):
    k = 0
    for j in range(i,i+B-1):
        k += b[j]
        if k > N:
            break
        if k not in Dict_b:
            Dict_b[k] = 1
        else:
            Dict_b[k] += 1
if Sum_a in Dict_a:
    Dict_a[Sum_a] += 1
else:
    Dict_a[Sum_a] = 1
if Sum_b in Dict_b:
    Dict_b[Sum_b] += 1
else:
    Dict_b[Sum_b] = 1
cnt = 0
for i in Dict_a:
    if N-i in Dict_b:
        cnt += Dict_a[i]*Dict_b[N-i]
if N in Dict_a:
    cnt += Dict_a[N]
if N in Dict_b:
    cnt += Dict_b[N]
print(cnt)