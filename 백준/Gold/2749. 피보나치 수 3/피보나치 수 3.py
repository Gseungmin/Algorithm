import sys
input = sys.stdin.readline
Fib = [0,1]
N = int(input())
for i in range(N-1):
    num = (Fib[-1]+Fib[-2])%1000000
    if num == 1:
        if Fib[-1] == 0:
            Fib.pop()
            break
    Fib.append(num)
    
print(Fib[N%len(Fib)])