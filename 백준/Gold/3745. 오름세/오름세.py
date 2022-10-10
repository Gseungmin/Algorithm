import sys
from bisect import bisect_left
input = sys.stdin.readline
while True:
    try:
        N = int(input())
    except Exception:
        break
    if N == 0:
        break
    arr = list(map(int,input().split()))
    List = [0]
    for num in arr:
        if List[-1] < num:
            List.append(num)
        else:
            List[bisect_left(List, num)] = num
    print(len(List)-1)