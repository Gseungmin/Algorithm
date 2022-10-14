import sys
input = sys.stdin.readline
N = int(input())
time = [0]
price = [0]
Max = []
for i in range(N):
    t, p = map(int,input().split())
    time.append(t)
    price.append(p)

def work_out(N, day, time, price, Sum, Max):
    if day > N:
        Max.append(Sum)
        return
    if day + time[day] > N+1:
        work_out(N, day+1, time, price, Sum, Max)
    else:
        work_out(N, day + time[day], time, price, Sum+price[day], Max)
        work_out(N, day+1, time, price, Sum, Max)
    return

work_out(N, 1, time, price, 0, Max)
print(max(Max))