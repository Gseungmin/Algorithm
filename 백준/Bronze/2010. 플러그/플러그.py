N = int(input())
sum = 0
for i in range(N):
    plug = int(input())
    sum += plug - 1
sum += 1
print(sum)