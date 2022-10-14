N, K = map(int,input().split())
Set = set()
Set.add("a")
Set.add("n")
Set.add("t")
Set.add("i")
Set.add("c")
def RC(index):
    if len(Set) == K:
        cnt = 0
        for i in List:
            check = 0
            for j in i:
                if j not in Set:
                    check = 1
                    break
            if check == 0:
                cnt += 1
        ans[0] = max(ans[0], cnt)
        return
    if index == 21:
        return
    Set.add(alpha[index])
    RC(index+1)
    Set.remove(alpha[index])
    RC(index+1)
    return
if len(Set) > K:
    print(0)
    exit()
alpha = ["b","d","e","f","g","h","j","k","l","m","o","p","q","r","s","u","v","w","x","y","z"]
ans = [0]
List = []
for _ in range(N):
    S = set(input())
    List.append(S)
RC(0)
print(ans[0])