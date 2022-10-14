import sys
input = sys.stdin.readline
P, K = map(str,input().split())
K = int(K)
true = [False]*(K+1)
for i in range(2,K+1):
    if true[i] == False:
        j = i
        while i*j <= K:
            true[i*j] = True
            j += 1

for i in range(2,K):
    if int(P) % i == 0:
        print("BAD", i)
        sys.exit()
print("GOOD")