S = input() #sentence including "(" or ")"
stack = [] #empty stack for taking "("
Sum = 0 #answer
iron = 0
true = 0 #condition for checking ) happens right after (
for k in S: #eack word in S
    if k == "(":
        true = 1
        stack.append(k)
        iron += 1
    else:
        if true == 1: #) happens right after (
            stack.pop(-1)
            iron -= 1
            Sum += iron
            true = 0
        else: #) happens consecutively
            stack.pop(-1)
            iron -= 1 
            Sum += 1
print(Sum)