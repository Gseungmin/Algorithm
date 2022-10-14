import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M = map(int,input().split())
arr = [i for i in range(N+1)]

def Find(x, List):
    if List[x] == x:
        return x
    y = Find(List[x], List)
    List[x] = y
    return y

def Union(x, y, List):
    a = Find(x, List)
    b = Find(y, List)
    if a == b:
        return
    if a < b:
        List[b] = a
    else:
        List[a] = b
    return

for i in range(M):
    k, a, b = map(int,input().split())
    if k == 0:
        Union(a, b, arr)
    else:
        x = Find(a, arr)
        y = Find(b, arr)
        if x == y:
            print("YES")
        else:
            print("NO")