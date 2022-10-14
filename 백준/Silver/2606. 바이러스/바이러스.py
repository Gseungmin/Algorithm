import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
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
    a, b = map(int,input().split())
    Union(a, b, arr)
    
ans = 0
for i in range(2,N+1):
    if arr[i] == 1 or Find(arr[i], arr) == 1:
        ans += 1
print(ans)