L = int(input())
p = input()

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

pi = getPi(p)
print(L-pi[-1])