import sys
input = sys.stdin.readline
stack = []
while 1:
    #입력 조건
    command = list(map(str,input().split()))

    #Write가 나왔을 경우
    if command[0] == "WRITE":
        check = True
        a, b = command[1], command[3]
        
        #스택의 값 탐색하면서 wait이 들어가야 하는지 판단
        for i in range(len(stack)-1,-1,-1):
            c = stack[i]
            if c[0] == "WAIT": #명령어를 수행할 수 있음
                break
            if c[0] == "WRITE": #WRITE에서 명령어를 수행할 수 없는 경우인지 판단
                x, y = stack[i][1], stack[i][3]

                #교착 상태, check
                if a == y and b == x:
                    check = False
                    break
                
                #똑같은 명령어 실행, check
                if a == x and b == y:
                    check = False
                    break
                
                #삽입되는 메모리가 확실하지 않은 경우, check
                if b == y:
                    check = False
                    break
                
                #삽입되는 메모리가 확실하지 않은 경우, check
                if a == y or x == b:
                    check = False
                    break
            
            if c[0] == "READ": #READ에서 명령어를 수행할 수 없는 경우인지 판단
                x = stack[i][1]
                
                if b == x:
                    check = False
                    break
        
        if check == False:
            stack.append(["WAIT"])
        stack.append(command)
                
    #Read가 나왔을 경우
    elif command[0] == "READ":
        check = True
        a = command[1]
        
        #스택의 값 탐색하면서 wait이 들어가야 하는지 판단
        for i in range(len(stack)-1,-1,-1):
            c = stack[i]
            if c[0] == "WAIT": #명령어를 수행할 수 있음
                break
            if c[0] == "WRITE": #WRITE에서 명령어를 수행할 수 없는 경우인지 판단
                x, y = stack[i][1], stack[i][3]
                
                #Write와 동시 실행
                if a == y:
                    check = False
                    break
        
        if check == False:
            stack.append(["WAIT"])
        stack.append(command)

    #종료 조건
    if command[0] == "EXIT":
        stack.append(command)
        break

for i in stack:
    print(" ".join(i))