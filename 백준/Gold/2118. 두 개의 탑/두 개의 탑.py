import sys
input = sys.stdin.readline
    
N = int(input())
dist_from_1 = [0]*(N+1)
for i in range(1,N+1):
    dist_from_1[i] = dist_from_1[i-1] + int(input())

x = 0
y = 1
ans = 0
while x < N:
    
    if x < y < N:
        right = dist_from_1[y] - dist_from_1[x]
        left = dist_from_1[N] - right
        if right == left:
            ans = right
            break
        elif right > left:
            ans = max(ans, left)
            x += 1
            if x == y:
                y += 1
        elif right < left:
            ans = max(ans,right)
            y += 1
            
    if x == N or y == N:
        break
print(ans)