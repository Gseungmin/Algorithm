import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    a, b = map(int,input().split())
    b = -b
    arr.append([a,b])
arr.sort()

graph = [[] for i in range(N)]
for i in range(len(arr)):
    a, b = arr[i][0], -arr[i][1]
    
    for j in range(len(graph)):
        if len(graph[j]) == 0:
            graph[j].append([a,b])
            break
        else:
            if graph[j][-1][-1]+1 == a:
                graph[j][-1][-1] = b
                break
            elif graph[j][-1][-1] < a:
                graph[j].append([a,b])
                break

cal = [0]*366
for i in range(N):
    for j in graph[i]:
        a, b = j
        for k in range(a, b+1):
            cal[k] = i+1

left = 0
right = 0
ans = 0
while left <= 365:
    if cal[left] == 0:
        left += 1
        right = max(left, right)
    else:
        Max = 0
        for right in range(left, 366):
            Max = max(Max, cal[right])
            if cal[right] == 0:
                break
            
        if cal[right] == 0:
            ans += (right-left)*Max
            left = right
        else:
            if right == 365:
                ans += (366-left)*Max
                break

print(ans)