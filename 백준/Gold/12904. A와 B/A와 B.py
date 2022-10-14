S = input()
T = input()
while 1:
    if T[-1] == 'A':
        T = T[:len(T)-1]
    else:
        T = T[:len(T)-1]
        T = T[::-1]
    if T == S:
        print(1)
        exit()
    if T == "":
        print(0)
        exit()