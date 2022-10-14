import sys
input = sys.stdin.readline
N = int(input())
seq = list(map(int,input().split()))
pl, mi, mul, div = map(int,input().split())
ans = []
def select(N, seq, index, total, pl, mi, mul, div, ans):
    if index >= N:
        ans.append(total)
        return
    if pl != 0:
        select(N, seq, index+1, total+seq[index], pl-1, mi, mul, div, ans)
    if mi != 0:
        select(N, seq, index+1, total-seq[index], pl, mi-1, mul, div, ans)
    if mul != 0:
        select(N, seq, index+1, total*seq[index], pl, mi, mul-1, div, ans)
    if div != 0:
        if seq[index] > 0 and total < 0:
            select(N, seq, index+1, -((-total)//seq[index]), pl, mi, mul, div-1, ans)
        else:
            select(N, seq, index+1, total//seq[index], pl, mi, mul, div-1, ans)
    return
select(N, seq, 1, seq[0], pl, mi, mul, div, ans)
ans.sort()
print(ans[-1])
print(ans[0])