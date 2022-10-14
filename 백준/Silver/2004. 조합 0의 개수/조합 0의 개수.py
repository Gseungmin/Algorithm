import sys
input = sys.stdin.readline
N, M = map(int, input().split())
if M == 0:
    print(0)
else:
    ans = []
    List = [N, N-M, M]
    for j in List:
        two = 0
        five = 0
        m = 2
        n = 5
        while j >= m:
            two += j // m
            m *= 2
        while j >= n:
            five += j // n
            n *= 5
        ans.append(two)
        ans.append(five)
    print(min(ans[0] - ans[2] - ans[4], ans[1] - ans[3] - ans[5]))