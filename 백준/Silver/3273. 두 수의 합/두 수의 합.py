import sys
input = sys.stdin.readline
N = int(input())
if N == 1:
    print(0)
    sys.exit()
List = list(map(int,input().split()))
List.sort()
Dict = dict()
X = int(input())
left, right = 0, 1
ans = 0
while 1:
    k = List[left] + List[right]
    if k < X:
        right += 1
        if right == N:
            left += 1
            right = left + 1
        if right == N or left == N-1:
            break
    elif k == X:
        ans += 1
        right += 1
        if right == N:
            left += 1
            right = left+1
        if left == N-1 or right == N:
            break
    elif k > X:
        left += 1
        right = left + 1
        if left == N-1 or right == N:
            break
print(ans)