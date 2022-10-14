import sys
input = sys.stdin.readline
M = int(input())
List = []

prime = [0]*(M+1)
prime[0] = 1
prime[1] = 1
for i in range(2,M+1):
    if prime[i] == 0:
        List.append(i)
        j = i
        while i*j <= M:
            prime[i*j] = 1
            j += 1

N = len(List)
if N == 0:
    print(0)
    sys.exit()
cnt = 0
left = 0
right = 0
Sum = List[left]
while 1:
    if Sum == M:
        cnt += 1
        Sum -= List[left]
        left += 1
        if left == N:
            break
        right = max(left, right)
        if right == left:
            Sum = List[left]
    elif Sum > M:
        Sum -= List[left]
        left += 1
    elif Sum < M:
        right += 1
        if right == N:
            break
        Sum += List[right]
    if left == N:
        break
print(cnt)