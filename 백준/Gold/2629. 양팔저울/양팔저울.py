import sys
input = sys.stdin.readline
N = int(input())
List = list(map(int,input().split()))
K = int(input())
arr = list(map(int,input().split()))
dp = [[set() for i in range(2)] for j in range(N)]
dp[0][1].add(List[0])
dp[0][0].add(0)
Dict = dict()
Dict[List[0]] = 1
for i in range(1,N):
    for j in dp[i-1][0]:
        Dict[j+List[i]] = 1
        Dict[j] = 1
        dp[i][1].add(j+List[i])
        dp[i][0].add(j)
    for j in dp[i-1][1]:
        Dict[j+List[i]] = 1
        Dict[j] = 1
        dp[i][1].add(j+List[i])
        dp[i][0].add(j)
ans = []
for i in arr:
    check = 0
    if i in Dict:
        ans.append("Y")
        check = 1
        continue
    for j in Dict:
        if i+j in Dict:
            ans.append("Y")
            check = 1
            break
    if check == 0:
        ans.append("N")
print(" ".join(ans))