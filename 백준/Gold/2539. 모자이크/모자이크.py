N, M = map(int,input().split())
K = int(input())
T = int(input())
List = []
Max = 0
for t in range(T):
    a, b = map(int,input().split())
    Max = max(Max,a)
    List.append([b,a])
List.sort()
left = Max
ans = 0
right = 1000000
while left <= right:
    mid = (left+right)//2
    check = True
    if Max > mid:
        right = mid-1
        continue
    if M < mid:
        right = mid-1
        continue
    index = 0
    cnt = 0
    for i in List:
        if i[0] >= index:
            index = i[0]+mid
            cnt += 1
        else:
            continue
    if cnt > K:
        check = False
    if check == True:
        right = mid-1
        ans = mid
    else:
        left = mid+1
print(ans)