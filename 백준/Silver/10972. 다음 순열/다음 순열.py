import sys
input = sys.stdin.readline
N = int(input()) #size of per
per = list(map(int,input().split()))
def Permutation(N, per):
    true = 0 #checking for last Permutation
    for index in range(N-1,0,-1):
        if per[index] > per[index-1]:
            change = index - 1
            true = 1
            break
    if true == 0: #if per is last Permutation
        print(-1)
        return
    for index in range(N-1, change, -1):
        if per[index] > per[change]:
            per[index], per[change] = per[change], per[index]
            break
    i = change + 1
    j = N - 1
    while i < j:
        per[i], per[j] = per[j], per[i]
        i += 1
        j -= 1
    for k in per:
        print(k, end = " ")
    return
Permutation(N, per)