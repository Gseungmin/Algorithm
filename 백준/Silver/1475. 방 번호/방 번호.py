List = [0]*9
N = list(input())
for i in N:
    if int(i) == 9:
        List[6] += 1
    else:
        List[int(i)] += 1
if List[6] % 2 == 0:
    List[6] = List[6] // 2
else:
    List[6] = (List[6] // 2) + 1
print(max(List))