import sys
input = sys.stdin.readline
N = int(input())
eggs = [list(map(int,input().split())) for i in range(N)]

cnt = [0]
def RC(index, N, eggs, cnt):
    if index == N:
        total = 0
        for i in eggs:
            if i[0] <= 0:
                total += 1
        cnt[0] = max(cnt[0], total)
        return
    if eggs[index][0] <= 0:
        RC(index+1, N, eggs, cnt)
    else:
        check = 0
        for i in range(N):
            if i == index:
                continue
            if eggs[i][0] <= 0:
                continue
            check = 1
            eggs[index][0], eggs[i][0] = eggs[index][0]-eggs[i][1], eggs[i][0]-eggs[index][1]
            RC(index+1, N, eggs, cnt)
            eggs[index][0], eggs[i][0] = eggs[index][0]+eggs[i][1], eggs[i][0]+eggs[index][1]
        if check == 0:
            cnt[0] = max(cnt[0], N-1)
            return
    return

RC(0, N, eggs, cnt)
print(cnt[0])