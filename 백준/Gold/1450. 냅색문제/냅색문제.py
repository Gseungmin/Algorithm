import sys
input = sys.stdin.readline
from bisect import bisect_right
N, C = map(int,input().split())
List = list(map(int,input().split()))
left = List[:N//2]
right = List[N//2:]

left_sum = []
def RC_left(arr, index, k):
    if index == len(arr):
        left_sum.append(k)
        return
    RC_left(arr, index+1, k+left[index])
    RC_left(arr, index+1, k)
    return

RC_left(left, 0, 0)
left_sum.sort()
ans = [0]

def RC_right(arr, index, k):
    if k > C:
        return
    if index == len(arr):
        ans[0] += bisect_right(left_sum, C-k)
        return
    RC_right(arr, index+1, k+right[index])
    RC_right(arr, index+1, k)
    return

RC_right(right, 0, 0)
print(ans[0])