import sys
input = sys.stdin.readline
N = int(input())
L = list(map(int,input().split()))
L.sort()
M = int(input())
List = list(map(int,input().split()))
true = [0]*M

from bisect import bisect_left, bisect_right
for i in range(len(List)):
    true[i] = abs(bisect_left(L,List[i]) - bisect_right(L,List[i])) 
print(" ".join(map(str,true)))