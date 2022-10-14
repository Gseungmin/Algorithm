import sys
input = sys.stdin.readline
N, K = map(int,input().split())
arr = list(map(int,input().split()))
mid = N//2
ans = int(1e9)
left = arr[:mid]
right = arr[mid:]
ans = [0]
Dict = dict()
def RC_l(index):
    if index == len(left):
        if List:
            value = sum(List)
            if value in Dict:
                Dict[value] += 1
            else:
                Dict[value] = 1
        else:
            if 0 in Dict:
                Dict[0] += 1
            else:
                Dict[0] = 1
        return
    List.append(left[index])
    RC_l(index+1)
    List.pop()
    RC_l(index+1)
    return

def RC_r(index):
    if index == len(right):
        if List:
            value = sum(List)
            if K-value in Dict:
                ans[0] += Dict[K-value]
        else:
            if K != 0:
                if K in Dict:
                    ans[0] += Dict[K]
            else:
                if K in Dict:
                    ans[0] += Dict[K]-1
        return
    List.append(right[index])
    RC_r(index+1)
    List.pop()
    RC_r(index+1)
    return

List = []
RC_l(0)
List = []
RC_r(0)

print(ans[0])