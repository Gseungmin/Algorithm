import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break
postorder = []

def post(left, right):
    if left > right:
        return
    root = preorder[left]
    mid = right+1
    for i in range(left+1,right+1):
        if preorder[i] > root:
            mid = i
            break
    post(left+1, mid-1)
    post(mid, right)
    postorder.append(root)
    return
post(0, len(preorder)-1)
for i in postorder:
    print(i)