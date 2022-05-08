import sys
input = sys.stdin.readline
N, C = map(int,input().split())
List = list(map(int,input().split()))
m = len(List)//2
front = List[:m]
back = List[m:]
case = []
case2 = []
def RC(index, num):
    if num > C:
        return
    if index == len(back):
        case.append(num)
        return
    RC(index+1, num+back[index])
    RC(index+1, num)
    return

def RC2(index, num):
    if num > C:
        return
    if index == len(front):
        case2.append(num)
        return
    RC2(index+1, num+front[index])
    RC2(index+1, num)
    return

RC(0,0)
RC2(0,0)
case.sort()
ans = 0
for i in case2:
    left = 0
    right = len(case)-1
    k = -1
    while left<=right:
        mid = (left+right)//2
        if case[mid]+i <= C:
            k = mid
            left = mid+1
        else:
            right = mid-1
    ans += (k+1)
print(ans)