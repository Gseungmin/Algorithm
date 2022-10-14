input_list = list()


while(1):
    n = int(input())
    if n:
        input_list.append(n)
    else:
        for tmp in input_list:
            r=1
            for n in range(2*tmp,tmp,-1):
                r *= n
            for n in range(1,tmp+2):
                r //= n
            print(r)
        break