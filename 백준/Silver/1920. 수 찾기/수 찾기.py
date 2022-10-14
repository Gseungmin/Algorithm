N = int(input())
num_A = list(map(int,input().split()))
M = int(input())
num_B = list(map(int,input().split()))
num_A.sort()
for i in range(len(num_B)):
    start = 0
    end = len(num_A) - 1
    In = 0
    while start <= end:
        mid = (start + end) // 2
        if num_A[mid] == num_B[i]:
            In = 1
            break
        elif num_A[mid] > num_B[i]:
            end = mid - 1
        elif num_A[mid] < num_B[i]:
            start = mid + 1
    if In == 1:
        print(1)
    else:
        print(0)