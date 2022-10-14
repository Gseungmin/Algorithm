def Seven(n):
    List = []
    for i in range(9):
        List.append(int(input()))
    Sum_List = sum(List)
    for i in range(len(List)-1):
        for j in range(i+1,len(List)):
            if Sum_List - List[i] - List[j] == 100:
                List.pop(j)
                List.pop(i) 
                return List
    return
answer = Seven(9)
answer.sort()
for i in answer:
    print(i)
