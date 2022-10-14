def getPi(p):
    N = len(p)
    pi = [0]*N
    j = 0
    for i in range(1,N):
        while j>0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            pi[i] = j+1
            j += 1
        else:
            pi[i] = 0
    return pi

def kmc(s,p):
    pi = getPi(p)
    ans = []
    N, M, j = len(s), len(p), 0
    for i in range(N):
        while j>0 and s[i] != p[j]:
            j = pi[j-1]
        if s[i] == p[j]:
            if j == M-1:
                ans.append(i-M+2)
                j = pi[j]
            else:
                j += 1
    return ans
    
s = input()
p = input()
ans = kmc(s,p)
print(len(ans))
if ans:
    print(" ".join(map(str,ans)))