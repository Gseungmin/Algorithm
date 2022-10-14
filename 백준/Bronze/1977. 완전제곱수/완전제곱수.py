M = int(input())
N = int(input())
Sum = []
i = 1
while True:
    if i*i >= M:
        if i*i <= N:
            Sum.append(i*i)
            i += 1
        else:
            break
    else:
        i += 1
if len(Sum) > 0:
    print(sum(Sum))
    print(Sum[0])
else:
    print(-1)