T = int(input())
from collections import deque
for _ in range(T):
    a = 0
    k = input()
    N = int(input())
    nums = deque(input().split(","))
    check = 0
    nums[0] = nums[0][1:]
    nums[-1] = nums[-1][:-1]
    if nums[0] == "":
        nums.popleft()
    for i in k:
        if i == "R":
            a = abs(1-a)
        else:
            if a == 0:
                if nums:
                    nums.popleft()
                else:
                    check = 1
                    break
            else:
                if nums:
                    nums.pop()
                else:
                    check = 1
                    break
    if check == 1:
        print("error")
    else:
        if a == 0:
            Str = "[" + ",".join(nums) + "]"
        else:
            Str = "[" + ",".join(list(nums)[::-1]) + "]"
        print(Str)