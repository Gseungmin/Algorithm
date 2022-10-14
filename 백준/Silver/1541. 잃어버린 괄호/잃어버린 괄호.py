import sys
input = sys.stdin.readline
Str = input() + "-"
l = 0
r = 0
total = 0
check = 0
if Str[0] == "-":
    check = 1
    l = 1
    r = 1
    n_list = []
while r < len(Str):
    if Str[r] == "+":
        if check == 1:
            n_list.append(int(Str[l:r]))
        else:
            total += int(Str[l:r])
        l = r+1
    elif Str[r] == "-":
        if check == 1:
            n_list.append(int(Str[l:r]))
            total -= sum(n_list)
        else:
            check = 1
            total += int(Str[l:r])
        l = r+1
        n_list = []
    r += 1
print(total)