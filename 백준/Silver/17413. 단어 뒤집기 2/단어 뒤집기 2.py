S = input() #sentence
S += " "
stack = []
true = 0 #condition for checking word in between < and >
for i in S: #each word in S
    if i == '<': #if i is <
        if stack: #if stack is not empty
            while stack:
                print(stack.pop(-1), end = "")
            print(i, end = "")
            true = 1
        else: #if stack is empty
            true = 1 #in this condition Don't turn sentencce upside down
            print('<', end = "")
    elif i == '>': #if i is >
        true = 0 #in this condition Turn sentencce upside down
        print('>', end = "")
    elif i == " ": #if i is empty space
        if true == 1:
            print(i, end = "")
        else:
            while stack:
                print(stack.pop(-1), end = "")
            print(i, end = "")
    else: #if i is word:
        if true == 1:
            print(i, end = "")
        else:
            stack.append(i)