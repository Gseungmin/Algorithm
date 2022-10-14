Tree, Needs = map(int,input().split())
Height = list(map(int,input().split()))
def tree_cutting(Needs,Height):
    Min = 0
    Max = max(Height)
    while Min <= Max:
        Mean = (Min + Max) // 2
        Sum = 0
        for i in range(len(Height)):
            if Height[i] - Mean > 0:
                Sum += Height[i] - Mean
        if Sum == Needs:
            return Mean
        if Sum > Needs:
            Min = Mean + 1
        elif Sum < Needs:
            Max = Mean - 1
    return Max
print(tree_cutting(Needs,Height))