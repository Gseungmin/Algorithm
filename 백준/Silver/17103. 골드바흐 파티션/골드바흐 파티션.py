import sys
input = sys.stdin.readline
true = [0]*1000001
for i in range(2,1001):
    j = i
    while i*j <= 1000000:
        true[i*j] = 1
        j += 1
        
T = int(input())
for _ in range(T):
    N = int(input())
    cnt = 0
    for i in range(2,N+1):
        if true[i] == 0:
            if true[N-i] == 0:
                if i > N-i:
                    print(cnt)
                    break
                cnt += 1