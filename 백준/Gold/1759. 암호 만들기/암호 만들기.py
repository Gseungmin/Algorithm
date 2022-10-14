import sys
input = sys.stdin.readline
N, C = map(int,input().split())
M = N
seq = list(map(str,input().split()))
seq.sort()
def password(seq, N, M, index, ans, C):
    if M == 0:
        ja = 0
        mo = 0
        for word in ans:
            if (word == 'a') or (word == 'e') or (word == 'i') or (word == 'o') or (word == 'u'):
                mo += 1
            else:
                ja += 1
        if (ja>=2) and (mo>=1):
            for k in range(N):
                if k == N-1:
                    print(ans[k])
                else:
                    print(ans[k], end = "")
        return
    if index >= C:
        return
    ans.append(seq[index])
    password(seq, N, M-1, index+1, ans, C) #pick
    ans.pop(-1)
    password(seq, N, M, index+1, ans, C) #not pick
    return

password(seq, N, M, 0, [], C)