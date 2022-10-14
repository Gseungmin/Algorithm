S = input()
K = input()
stack = []
for i in range(len(S)):
    stack.append(S[i])
    while len(stack) >= len(K) and stack[-1] == K[-1]:
        N = len(K)
        index = -1
        check = 0
        while -index <= N:
            if stack[index] != K[index]:
                check = 1
                break
            index -= 1
        if check == 0:
            for j in range(N):
                stack.pop()
        else:
            break
if stack:
    print("".join(stack))
else:
    print("FRULA")