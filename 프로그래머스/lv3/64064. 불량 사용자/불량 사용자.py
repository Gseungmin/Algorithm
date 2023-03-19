import sys
def solution(user_id, banned_id):
    count = dict()
    for i in banned_id:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    pos = dict()
    for i in user_id:
        pos[i] = set()
        for j in banned_id:
            if len(i) != len(j):
                continue
            check = True
            for k in range(len(i)):
                if j[k] == "*":
                    continue
                if j[k] != i[k]:
                    check = False
                    break
            if check == True:
                pos[i].add(j)
    ans = dict()
    arr = [0]*len(user_id)
    h = [0]
    def RC(index, cnt, List):
        if cnt == len(banned_id):
            ans[tuple(List)] = True
            return
        if index == len(user_id):
            return
        name = user_id[index]
        for i in pos[name]:
            if count[i] != 0:
                count[i] -= 1
                arr[index] = i
                List.append(name)
                RC(index+1,cnt+1,List)
                List.pop()
                arr[index] = 0
                count[i] += 1
        RC(index+1,cnt,List)
        return
    RC(0,0,[])
    return len(ans)