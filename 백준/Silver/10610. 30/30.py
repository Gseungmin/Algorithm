N = list(map(int,list(input())))
N.sort()
if sum(N)%3 != 0 or N[0] != 0:
    print(-1)
else:
    ans = ""
    for i in range(len(N)-1,-1,-1):
        ans += str(N[i])
    print(int(ans))