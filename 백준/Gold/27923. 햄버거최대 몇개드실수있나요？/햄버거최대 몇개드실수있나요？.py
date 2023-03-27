#1:58

#다양한 햄버거를 먹으며 햄최몇 측정
#N개의 햄버거
#질량만큼 위속 질량 증가
#원하는 순서대로 먹을 수 있음
#k개의 콜라, 콜라를 먹으면 그 후 l개를 먹는 동안 콜라효과를 얻음, 효과 중첩가능
#질량이 m인 햄버거를 콜라 효과가 C번 중첩되면 m//(2**c)만큼 위속의 질량이 증가함
#필요한 위의 용량 최솟값
#누적합 문제

N, K, L = map(int,input().split())
burger = list(map(int,input().split()))
coke = list(map(int,input().split()))

index = [0]*(N+1)
for i in coke:
    index[i] += 1
    if i+L <= N:
        index[i+L] -= 1

ans = 0

#최대 값 추출
arr = []
Sum = 0
for i in range(1,N+1):
    Sum += index[i]
    arr.append(Sum)
arr.sort(reverse=True)
burger.sort(reverse=True)

#최소 질량
for i in range(len(arr)):
    ans += burger[i]//(2**arr[i])

print(ans)