S = input() #문장
alpha = [-1]*26
for k in range(len(S)):
    if alpha[ord(S[k])-97] == -1: #아직 발견되기 전이면
        alpha[ord(S[k])-97] = k
print(" ".join(map(str, alpha)))