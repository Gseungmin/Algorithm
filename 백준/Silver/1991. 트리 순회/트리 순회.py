import sys
input = sys.stdin.readline
N = int(input())
Tree = dict()
for i in range(N):
    a, b, c = map(str,input().split())
    Tree[a] = [b,c]

def Pre(x, S):
    S.append(x)
    for nx in Tree[x]:
        if nx == ".":
            continue
        Pre(nx, S)
    return

def In(x, S):
    if Tree[x][0] != ".":
        In(Tree[x][0], S)
    S.append(x)
    if Tree[x][1] != ".":
        In(Tree[x][1], S)
    return

def Post(x, S):
    for nx in Tree[x]:
        if nx == ".":
            continue
        Post(nx, S)
    S.append(x)
    return

S = []
Pre("A", S)
print("".join(S))
S = []
In("A", S)
print("".join(S))
S = []
Post("A", S)
print("".join(S))