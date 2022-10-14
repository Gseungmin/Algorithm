import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
if M == 0:
    print(min(len(str(N)), abs(N-100)))
    sys.exit()
Set = set(map(int,input().split()))

if N == 100:
    print(0)
    sys.exit()

def plus(N, Set):
    cnt = 0
    for i in range(N, 1000001):
        Str = str(i)
        true = 0
        for j in range(len(Str)):
            if int(Str[j]) in Set:
                cnt += 1
                true = 1
                break
        if true == 0:
            return cnt + len(Str)
    return -1


def minus(N, Set):
    cnt = 0
    for i in range(N, -1, -1):
        Str = str(i)
        true = 0
        for j in range(len(Str)):
            if int(Str[j]) in Set:
                cnt += 1
                true = 1
                break
        if true == 0:
            return cnt + len(Str)
    return -1
    
p = plus(N, Set)
m = minus(N, Set)
if p == -1 and m != -1:
    print(min(m, abs(N-100)))
elif p != -1 and m == -1:
    print(min(p, abs(N-100)))
elif p != -1 and m != -1:
    print(min(p,m,abs(N-100)))
else:
    print(abs(N-100))