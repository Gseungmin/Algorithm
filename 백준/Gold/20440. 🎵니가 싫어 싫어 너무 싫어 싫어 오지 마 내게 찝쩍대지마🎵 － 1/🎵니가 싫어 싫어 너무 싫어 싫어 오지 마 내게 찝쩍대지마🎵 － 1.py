import sys
input = sys.stdin.readline
N = int(input())
in_room = dict()
out_room = dict()
in_list = []
out_list = []

All = set()
for i in range(N):
    a, b = map(int,input().split())
    in_list.append(a)
    out_list.append(b)
    All.add(a)
    All.add(b)

in_list.sort()
out_list.sort()
for i in range(N):
    a, b = in_list[i], out_list[i]
    if a in in_room:
        in_room[a] += 1
    else:
        in_room[a] = 1
    if b in out_room:
        out_room[b] += 1
    else:
        out_room[b] = 1

All = list(All)
All.sort()
cnt = 0
ans = 0
for i in All:
    k = 0
    if i in in_room:
        k += in_room[i]
    if i in out_room:
        k -= out_room[i]
    if k > 0:
        ans = max(ans, cnt+k)
    cnt += k

print(ans)
check = False
for i in All:
    k = 0
    if i in in_room:
        k += in_room[i]
    if i in out_room:
        k -= out_room[i]
    cnt += k
    if cnt == ans:
        if check == False:
            check = True
            print(i, end = " ")
    if cnt < ans and check == True:
        print(i)
        sys.exit()