import sys
input = sys.stdin.readline
N = int(input())
Set = set()
for i in range(N+1):
    for j in range(N+1-i):
        for k in range(N+1-i-j):
            l = N-i-j-k
            Set.add(i*1+j*5+k*10+l*50)
print(len(Set))