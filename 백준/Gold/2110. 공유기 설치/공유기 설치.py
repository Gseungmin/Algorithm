import sys
input = sys.stdin.readline
N, C = map(int,input().split())
List = [int(input()) for i in range(N)]
List.sort()
right = List[-1] - List[0]
left = 1
def cnt(List, num):
    total = 1
    i = 0
    j = 1
    length = len(List)
    while j < length:
        if List[j] - List[i] >= num:
            i = j
            j += 1
            total += 1
        else:
            j += 1
    return total
    
def P2110(N, C, List, left, right):
    while left <= right:
        mid = (left+right)//2
        total = cnt(List, mid)
        if total < C: #정답이 아닌 경우가 아닌 가능성이 완전 없는 경우
            right = mid - 1
        else: #정답인 경우가 아닌 가능성이 있는 경우
            ans = mid #mid가 답이라고 가정한다.
            left = mid + 1
    return ans

ans = P2110(N, C, List, left, right)
print(ans)