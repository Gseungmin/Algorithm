num = input()
INF = int(1e9)
def div(num):
    if len(num) == 1:
        if int(num)%2 == 0:
            return 0
        else:
            return 1
    if len(num) == 2:
        k = 0
        for i in range(len(num)):
            if int(num[i]) % 2 == 1:
                k += 1
        nn = str(int(num[0])+int(num[1]))
        m = div(nn)
        k += m
        return k
    L = len(num)
    k = 0
    for i in num:
        if int(i) % 2 == 1:
            k += 1
    v = 0
    for a in range(L-2):
        for b in range(a+1,L-1):
            for c in range(b+1,L):
                num1 = num[:a+1]
                num2 = num[a+1:b+1]
                num3 = num[b+1:]
                v = max(v, div(str(int(num1)+int(num2)+int(num3))))
    return k+v
    
def div2(num):
    if len(num) == 1:
        if int(num)%2 == 0:
            return 0
        else:
            return 1
    if len(num) == 2:
        k = 0
        for i in range(len(num)):
            if int(num[i]) % 2 == 1:
                k += 1
        nn = str(int(num[0])+int(num[1]))
        m = div2(nn)
        k += m
        return k
    L = len(num)
    k = 0
    for i in num:
        if int(i) % 2 == 1:
            k += 1
    v = INF
    for a in range(L-2):
        for b in range(a+1,L-1):
            for c in range(b+1,L):
                num1 = num[:a+1]
                num2 = num[a+1:b+1]
                num3 = num[b+1:]
                v = min(v, div2(str(int(num1)+int(num2)+int(num3))))
    return k+v

print(div2(num), div(num))