import sys
input = sys.stdin.readline
M, N = map(int, input().split())
prime = [0]*(N+1) #Let's think all num is prime
prime[0] = 1 #exception case
prime[1] = 1 #exception case
for i in range(2,N+1):
    if prime[i] == 0: #if prime[i] is prime num
        j = i
        while i*j <= N:
            prime[i*j] = 1 #prime[i*j] is not prime num
            j += 1
for k in range(M, N+1):
    if prime[k] == 0:
        print(k)