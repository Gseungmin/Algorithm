import sys
input = sys.stdin.readline
N, H = map(int,input().split())
up = []
down = []
for i in range(N):
    if i % 2 == 0:
        up.append(int(input()))
    else:
        down.append(int(input()))

up.sort()
down.sort()

def BS(arr, h, left, right):
    while left <= right:
        mid = (left+right)//2
        if arr[mid] < h:
            left = mid+1
        else:
            right = mid-1
    return left

Min = N
Max = 0
for i in range(1,H+1):
    down_count = len(down) - BS(down, i-0.5, 0, len(down)-1)
    top_count = len(up) - BS(up, H-i+0.5, 0, len(up)-1)
    
    if Min == down_count + top_count:
        Max += 1
    elif Min > down_count + top_count:
        Max = 1
        Min = down_count + top_count
print(Min, Max)