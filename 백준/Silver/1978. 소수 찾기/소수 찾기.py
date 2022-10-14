import sys
input = sys.stdin.readline
N = int(input()) #primes
prime = list(map(int, input().split()))
Sum = 0
for k in prime:
    if k == 1:
        continue
    elif k == 2 or k == 3:
        Sum += 1
    else: # k >= 4
        i = 2
        true = 0 #contiodion for checking k is prime
        while i*i <= k:
            if k % i == 0: #if k has another divior
                true = 1
                break
            else:
                i += 1
        if true == 0:
            Sum += 1
print(Sum)