import sys
input = sys.stdin.readline
W, M, k = map(int,input().split())
team = min(W//2, M)
while k > 0:
    if team == W//2:
        while team != M:
            M -= 1
            k -= 1
    if team == M:
        while team*2 != W:
            W -= 1
            k -= 1
    if k <= 0:
        print(team)
        sys.exit()
    else:
        team -= 1
        k -= 3
        if k <= 0:
            print(team)
            sys.exit()
print(team)