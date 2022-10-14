import sys #for using sys
input = sys.stdin.readline
N = int(input()) #size of seq
seq = list(map(int, input().split())) #sequence
memo = [seq[0]]*N
for i in range(1,N):
    memo[i]= max(memo[i-1]+seq[i],seq[i])
print(max(memo))
