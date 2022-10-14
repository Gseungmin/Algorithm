while 1:
    S = input()
    if S[0] == ".":
        break
    left1 = 0 #"("
    left2 = 0 #")"
    right1 = 0 #"["
    right2 = 0 #"]"
    check = 0
    stack = []
    for i in S:
        if i == "(":
            left1 += 1
        elif i == "[":
            left2 += 1
        elif i == ")":
            right1 += 1
            if right1 > left1:
                check = 1
                break
        elif i == "]":
            right2 += 1
            if right2 > left2:
                check = 1
                break
        if i == "[" or i == "(" or i == "]" or i == ")":
            stack.append(i)
        if i == ")":
            if stack[-2] == "(":
                stack.pop()
                stack.pop()
                left1 -= 1
                right1 -= 1
            else:
                check = 1
                break
        elif i == "]":
            if stack[-2] == "[":
                left2 -= 1
                right2 -= 1
                stack.pop()
                stack.pop()
            else:
                check = 1
                break
    if check == 1 or left1 != 0 or left2 != 0 or right1 != 0 or right2 != 0:
        print("no")
    else:
        print("yes")