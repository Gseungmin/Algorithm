import sys
from bisect import bisect_left
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
List = [-1000000001]
for num in arr:
    if List[-1] < num:
        List.append(num)
    else:
        List[bisect_left(List, num)] = num
print(len(List)-1)