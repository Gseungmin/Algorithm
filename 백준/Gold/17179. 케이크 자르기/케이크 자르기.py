import sys
input = sys.stdin.readline
N, M, L = map(int,input().split())
spot = [0] + [int(input()) for i in range(M)] + [L]
left = 0
right = L

def BS(left, right, friends):
    ans = -1
    while left <= right:
        check = False
        index = 0
        cnt = 0
        mid = (left+right)//2
        for i in range(index+1,len(spot)):
            if spot[i]-spot[index] >= mid:
                cnt += 1
                index = i
            if cnt >= friends:
                check = True
                break
        if check == True:
            left = mid+1
            ans = mid
        else:
            right = mid-1
    return ans

for _ in range(N):
    print(BS(left, right, int(input())+1))