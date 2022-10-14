import sys
input = sys.stdin.readline
Fib = [0,1]
N = int(input())
for i in range(N-1):
    Fib.append(Fib[-1]+Fib[-2])
print(Fib[N])
