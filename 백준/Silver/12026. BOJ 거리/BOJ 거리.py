N = int(input())
Str = input()

d = [-1]*N
d[0] = 0
for i in range(1,N):
    for j in range(i):
        if Str[i] == "B":
            if Str[j] == "J":
                if d[j] == -1:
                    continue
                if d[i] == -1:
                    d[i] = d[j]+(i-j)**2
                else:
                    d[i] = min(d[i], d[j]+(i-j)**2)
        if Str[i] == "O":
            if Str[j] == "B":
                if d[j] == -1:
                    continue
                if d[i] == -1:
                    d[i] = d[j]+(i-j)**2
                else:
                    d[i] = min(d[i], d[j]+(i-j)**2)
        if Str[i] == "J":
            if Str[j] == "O":
                if d[j] == -1:
                    continue
                if d[i] == -1:
                    d[i] = d[j]+(i-j)**2
                else:
                    d[i] = min(d[i], d[j]+(i-j)**2)
print(d[N-1])