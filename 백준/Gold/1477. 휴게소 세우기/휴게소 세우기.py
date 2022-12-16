import sys
input = sys.stdin.readline
N, M, L = map(int,input().split())
loc = list(map(int,input().split()))

loc.sort()
loc.append(L)

left = 1
right = L
ans = 0
while left <= right:
    mid = (left+right)//2
    
    ## logic
    check = True
    
    ## init
    now, index, cnt = 0, 0, 0
    
    while index <= N:
        
        if now+mid < loc[index]:
            now += mid
            cnt += 1
        else:
            now = loc[index]
            index += 1
        
        if cnt > M:
            check = False
            break
    
    if check == True:
        right = mid-1
        ans = mid
    elif check == False:
        left = mid+1

print(ans)