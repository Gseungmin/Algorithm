N = int(input())
Set = set()
for i in range(N):
    a, b = input().split()
    if b == "enter":
        Set.add(a)
    if b == "leave":
        Set.discard(a)
List = list(Set)
List.sort(reverse = True)
for i in List:
    print(i)