import sys
input = sys.stdin.readline
import bisect

N = int(input())
List = list(map(int,input().split()))

ans = [List[0]]
for i in range(1,N):
    if List[i] > ans[-1]:
        ans.append(List[i])
    else:
        index = bisect.bisect_left(ans, List[i])
        ans[index] = List[i]
print(len(ans))