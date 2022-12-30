import sys
input = sys.stdin.readline
N, K, D = map(int,input().split())
List = [list(map(int,input().split())) for i in range(K)]
left = 1
right = N
ans = 0
while left <= right:
    mid = (left+right)//2
    
    count = 0
    check = False
    for a, b, c in List:
        if mid < a:
            continue
        elif a <= mid <= b:
            if ((mid-a)%c) == 0:
                check = True
            count += (((mid-a)//c)+1)
        elif mid > b:
            count += (((b-a)//c)+1)
            if ((b-a)%c) == 0:
                check = True
        if count > D:
            break
    
    if count < D:
        left = mid+1
    elif count >= D:
        if check == True:
            ans = mid
        right = mid-1
        
print(ans)