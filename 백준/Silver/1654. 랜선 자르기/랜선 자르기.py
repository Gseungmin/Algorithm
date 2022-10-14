import sys
input = sys.stdin.readline
K, N = map(int,input().split())
List = [int(input()) for i in range(K)]
List.sort()
right = List[-1]
left = 1
def cutting(List, num):
    total = 0
    for i in List:
        total = total + i//num
    return total
def P1654(N, K, List, left, right):
    while left <= right:
        mid = (left+right)//2
        total = cutting(List, mid)
        if total < N: #정답이 아닌 경우가 아닌 가능성이 완전 없는 경우
            right = mid - 1
        else: #정답인 경우가 아닌 가능성이 있는 경우
            ans = mid #mid가 답이라고 가정한다.
            left = mid + 1
    return ans

ans = P1654(N, K, List, left, right)
print(ans)