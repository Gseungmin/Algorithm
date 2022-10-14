import sys
input = sys.stdin.readline
N = int(input())
K = int(input())

def DaC(mid,N,K):
    index = 0
    for i in range(1,N+1):
        if mid//i <= N:
            if mid%i == 0:
                index += mid//i-1
            else:
                index += mid//i
        else:
            index += N
    return index+1


left = 1
right = N*N

while left <= right:
    mid = (left+right)//2
    index = DaC(mid,N,K)
    if index <= K:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)