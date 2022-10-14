N = int(input())
num_list = list(map(int,input().split()))
budget = int(input())
def Budget(budget,num_list):
    need = sum(num_list)
    if need <= budget:
        return max(num_list)
    min_value = 0
    max_value = max(num_list)
    while min_value <= max_value:
        mean_value = (min_value + max_value) // 2
        Sum = 0
        for i in range(len(num_list)):
            if num_list[i] - mean_value > 0:
                Sum += num_list[i] - mean_value
        if Sum == need - budget:
            return mean_value
        if Sum > need - budget:
            min_value = mean_value + 1
        else:
            max_value = mean_value - 1
    return max_value
print(Budget(budget,num_list))