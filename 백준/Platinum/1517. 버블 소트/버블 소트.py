import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
count = [0]

from collections import deque

def Merge(List1, List2, count):
    merge = deque()
    while List1 and List2:
        if List1[0] > List2[0]:
            merge.append(List2.popleft())
            count[0] += len(List1)
        else:
            merge.append(List1.popleft())
    while List1:
        merge.append(List1.popleft())
    while List2:
        merge.append(List2.popleft())
    return merge

def DaC(A, count, start, end):
    if start == end:
        List3 = deque()
        List3.append(A[start])
        return List3
    mid = (start+end)//2
    List1 = DaC(A, count, start, mid)
    List2 = DaC(A, count, mid+1, end)
    merge = Merge(List1, List2, count)
    return merge
    
DaC(A, count, 0, N-1)
print(count[0])