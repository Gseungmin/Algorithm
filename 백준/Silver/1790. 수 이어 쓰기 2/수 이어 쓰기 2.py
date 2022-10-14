import sys
input = sys.stdin.readline
N, K = map(int,input().split())

def length(num):
    """1~num까지의 길이"""
    if num < 10:
        return num
    if num < 100:
        return 9 + (num-9)*2
    if num < 1000:
        return 9 + 90*2 + (num-99)*3
    if num < 10000:
        return 9 + 90*2 + 900*3 + (num-999)*4
    if num < 100000:
        return 9 + 90*2 + 900*3 + 9000*4 + (num-9999)*5
    if num < 1000000:
        return 9 + 90*2 + 900*3 + 9000*4 + 90000*5 + (num-99999)*6
    if num < 10000000:
        return 9 + 90*2 + 900*3 + 9000*4 + 90000*5 + 900000*6 + (num-999999)*7
    if num < 100000000:
        return 9 + 90*2 + 900*3 + 9000*4 + 90000*5 + 900000*6 + 9000000*7 + (num-9999999)*8
    if num == 100000000:
        return 9 + 90*2 + 900*3 + 9000*4 + 90000*5 + 900000*6 + 9000000*7 + 90000000*8 + 9

def P1790(K, left, right):
    check = 0
    while left <= right:
        mid = (left + right)//2
        index = length(mid)
        if index < K:
            left = mid + 1
        else:
            check = 1
            right = mid - 1
            ans = mid
    if check == 0:
        return -1
    return ans

ans = P1790(K, 1, N)
if ans == -1:
    print(-1)
else:
    print(list(str(ans))[K-length(ans-1)-1])