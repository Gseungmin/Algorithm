import sys
input = sys.stdin.readline
from math import *
N = int(input())
List = list(map(int,input().split()))
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
    return min(m1,m2)

def update(node, start, end, index, value):
    if start > index or end < index:
        return
    if start == end:
        segment[node] = value
        return
    mid = (start+end)//2
    update(node*2, start, mid, index, value)
    update(node*2+1, mid+1, end, index, value)
    segment[node] = min(segment[node*2], segment[node*2+1])
    return

SMT(1, 0, N-1)
M = int(input())
for i in range(M):
    a, b, c = map(int,input().split())
    if a == 2:
        print(query(1,0,N-1,b-1,c-1))
    else:
        update(1,0,N-1,b-1,c)