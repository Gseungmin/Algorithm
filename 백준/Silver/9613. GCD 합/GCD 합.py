import sys
input = sys.stdin.readline
T = int(input()) #testcase
for i in range(T):
    num_list = list(map(int, input().split()))
    GCD = 0
    for j in range(1,len(num_list)-1):
        for k in range(j+1,len(num_list)):
            a = num_list[j]
            b = num_list[k]
            while b != 0: #until k is 0
                a, b = b, a % b
            GCD += a
    print(GCD)