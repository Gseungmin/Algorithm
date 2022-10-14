import sys
S = input() #문장
alpha = [0]*26
for k in S:
    alpha[ord(k)-97] += 1
print(" ".join(map(str, alpha)))