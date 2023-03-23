def solution(expression):
    Str = ""
    oper_ = []
    num_ = []
    cnt = set()
    for i in expression:
        if i == "+" or i == "-" or i == "*":
            cnt.add(i)
            num_.append(int(Str))
            oper_.append(i)
            Str = ""
        else:
            Str += i
    num_.append(int(Str))
    import copy
    ans = 0
    if len(cnt) == 3:
        for a in ["+","-","*"]:
            for b in ["+","-","*"]:
                if a == b:
                    continue
                for c in ["+","-","*"]:
                    if a == c or b == c:
                        continue
                    num = copy.deepcopy(num_)
                    oper = copy.deepcopy(oper_)
                    i = 0
                    while 1:
                        if oper[i] == a:
                            oper.pop(i)
                            if a == "*":
                                num[i:i+2] = [num[i+1]*num[i]]
                            elif a == "+":
                                num[i:i+2] = [num[i+1]+num[i]]
                            elif a == "-":
                                num[i:i+2] = [num[i]-num[i+1]]
                        else:
                            i += 1
                        if i >= len(oper) or len(oper) == 0:
                            break
                    i = 0
                    while 1:
                        if oper[i] == b:
                            oper.pop(i)
                            if b == "*":
                                num[i:i+2] = [num[i+1]*num[i]]
                            elif b == "+":
                                num[i:i+2] = [num[i+1]+num[i]]
                            elif b == "-":
                                num[i:i+2] = [num[i]-num[i+1]]
                        else:
                            i += 1
                        if i >= len(oper) or len(oper) == 0:
                            break
                    i = 0
                    while 1:
                        if oper[i] == c:
                            oper.pop(i)
                            if c == "*":
                                num[i:i+2] = [num[i+1]*num[i]]
                            elif c == "+":
                                num[i:i+2] = [num[i+1]+num[i]]
                            elif c == "-":
                                num[i:i+2] = [num[i]-num[i+1]]
                        else:
                            i += 1
                        if i >= len(oper) or len(oper) == 0:
                            break
                    ans = max(ans,abs(num[0]))
    elif len(cnt) == 2:
        for a in cnt:
            for b in cnt:
                if a == b:
                    continue
                num = copy.deepcopy(num_)
                oper = copy.deepcopy(oper_)
                i = 0
                while 1:
                    if oper[i] == a:
                        oper.pop(i)
                        if a == "*":
                            num[i:i+2] = [num[i+1]*num[i]]
                        elif a == "+":
                            num[i:i+2] = [num[i+1]+num[i]]
                        elif a == "-":
                            num[i:i+2] = [num[i]-num[i+1]]
                    else:
                        i += 1
                    if i >= len(oper) or len(oper) == 0:
                        break
                i = 0
                while 1:
                    if oper[i] == b:
                        oper.pop(i)
                        if b == "*":
                            num[i:i+2] = [num[i+1]*num[i]]
                        elif b == "+":
                            num[i:i+2] = [num[i+1]+num[i]]
                        elif b == "-":
                            num[i:i+2] = [num[i]-num[i+1]]
                    else:
                        i += 1
                    if i >= len(oper) or len(oper) == 0:
                        break
                ans = max(ans,abs(num[0]))
    elif len(cnt) == 1:
        for a in cnt:
            num = copy.deepcopy(num_)
            oper = copy.deepcopy(oper_)
            i = 0
            while 1:
                if oper[i] == a:
                    oper.pop(i)
                    if a == "*":
                        num[i:i+2] = [num[i+1]*num[i]]
                    elif a == "+":
                        num[i:i+2] = [num[i+1]+num[i]]
                    elif a == "-":
                        num[i:i+2] = [num[i]-num[i+1]]
                else:
                    i += 1
                if i >= len(oper) or len(oper) == 0:
                    break
            ans = max(ans,abs(num[0]))
    return ans