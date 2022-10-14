import sys
input = sys.stdin.readline
N, M = map(int,input().split())
List = list(map(int,input().split()))
left, right = 0, 0
cnt = 0
Sum = List[left]
while 1:
    if Sum == M:
        cnt += 1
        Sum -= List[left]
        left += 1
        if left == N:
            break
        right = max(left, right)
        if right == left:
            Sum = List[left]
    elif Sum > M:
        Sum -= List[left]
        left += 1
    elif Sum < M:
        right += 1
        if right >= N:
            break
        Sum += List[right]
    if left >= N:
        break
print(cnt)