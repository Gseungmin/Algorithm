import sys
input = sys.stdin.readline

prime = [0]*(1000001)
prime[0], prime[1] = 1, 1
for i in range(2,1001):
    if prime[i] == 0:
        j = i
        while i*j < 1000001:
            prime[i*j], j = 1, j+1

while 1:
    A = int(input())
    if A == 0:
        sys.exit()
    true = 0
    for i in range(3, A+1, 2):
        if prime[A-i] == 0 and prime[i] == 0:
            true = 1
            print(A, "=", i, "+", A-i)
            break
    if true == 0:
        print("Goldbach's conjecture is wrong.")