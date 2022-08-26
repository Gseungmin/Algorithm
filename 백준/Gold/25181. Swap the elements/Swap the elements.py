import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
A = list(map(int,input().split()))

Nums = dict()
for i in range(len(A)):
    if A[i] in Nums:
        Nums[A[i]].add(i)
    else:
        Nums[A[i]] = set()
        Nums[A[i]].add(i)

def RC(index, List):
    if index == N:
        print(" ".join(map(str,List)))
        sys.exit()
    c1 = List[index] #바꿀 값
    for i in range(N):
        if i == index:
            continue
        c2 = List[i] #바꿔질 값
        if A[index] == c2:
            continue
        if A[i] == c1:
            continue
        List[i], List[index] = List[index], List[i]
        RC(index+1, List)
        List[i], List[index] = List[index], List[i]
    return

import copy
List = copy.deepcopy(A)
RC(0,List)
print(-1)