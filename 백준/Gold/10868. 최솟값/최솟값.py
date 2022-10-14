import sys
input = sys.stdin.readline
from math import *
N, M = map(int,input().split())
List = [int(input()) for i in range(N)]
h = int(ceil(log2(N)))
size = 1<<(h+1)
segment = [0]*size

def SMT(node, start, end):
    if start == end:
        segment[node] = List[start]
        return
    mid = (start+end)//2
    SMT(node*2, start, mid)
    SMT(node*2+1, mid+1, end)
    segment[node] = min(segment[node*2], segment[node*2+1])
    return

SMT(1,0,N-1)

def query(node, start, end, left, right):
    if end < left or start > right:
        return -1
    if left <= start and end <= right:
        return segment[node]
    mid = (start+end)//2
    m1 = query(node*2, start, mid, left, right)
    m2 = query(node*2+1, mid+1, end, left, right)
    if m1 == -1:
        return m2
    elif m2 == -1:
        return m1
    return min(m1, m2)

for i in range(M):
    a, b = map(int,input().split())
    print(query(1,0,N-1,a-1,b-1))