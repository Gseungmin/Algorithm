import sys
input = sys.stdin.readline
import heapq
R, C = map(int,input().split())
N = int(input())
List = [list(map(int,input().split())) for i in range(N)]
List.sort()

left = 1
right = int(1e9)
ans = int(1e9)
while left <= right:
    mid = (left+right)//2
    
    check = False
    
    if mid >= (R-1)+(C-1):
        check = True
    else:
        dp = [-1]*N #i번째를 방문
        for m in range(N):
            i, j, k = List[m]
            if (i-1) + (j-1) <= mid: #방문 가능하면
                dp[m] = mid-((i-1)+(j-1))+k
                
        for i in range(N):
            x1, y1, k1 = List[i][0], List[i][1], dp[i]
            if k1 != -1:
                if (R-x1)+(C-y1) <= k1:
                    check = True
                    break
                for j in range(N):
                    if i == j:
                        continue
                    x2, y2, k2 = List[j]
                    if x1 <= x2 and y1 <= y2:
                        if k1 >= (x2-x1)+(y2-y1):
                            dp[j] = max(dp[j], k1-((x2-x1)+(y2-y1))+k2)
                
    if check == True:
        right = mid-1
        ans = mid
    else:
        left = mid+1
        
print(ans)