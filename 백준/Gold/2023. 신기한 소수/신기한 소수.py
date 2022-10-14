import sys
input = sys.stdin.readline
N = int(input())

ans = []
def RC(index):
    k = int("".join(Str))
    for j in range(2,int(k**0.5)+1):
        if k % j == 0:
            return
    if index == N:
        ans.append(k)
        return
    posi = [1,3,7,9]
    for i in posi:
        Str.append(str(i))
        RC(index+1)
        Str.pop()
    return
List = [2,3,5,7]
for i in List:
    Str = [str(i)]
    RC(1)
for i in ans:
    print(i)