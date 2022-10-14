import sys
input = sys.stdin.readline

def RC(N, M, arr, ans, index):
    if M == 6:
        print(" ".join(map(str, ans)))
        return
    if index == N:
        return
    ans.append(arr[index])
    RC(N, M+1, arr, ans, index+1)
    ans.pop()
    RC(N, M, arr, ans, index+1)
    return

while 1:
    arr = list(map(int,input().split()))
    if arr[0] == 0:
        sys.exit()
    ans = []
    RC(arr[0],0,arr[1:],ans,0)
    print()