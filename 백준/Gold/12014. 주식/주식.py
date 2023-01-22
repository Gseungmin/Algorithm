import sys
from bisect import bisect_left
input = sys.stdin.readline

T = int(input())

for _ in range(1, T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))
    List = [0]
    for num in arr:
        if List[-1] < num:
            List.append(num)
        else:
            List[bisect_left(List, num)] = num
    Len = len(List)-1
    print("Case #" + str(_))
    if Len >= K:
        print(1)
    else:
        print(0)