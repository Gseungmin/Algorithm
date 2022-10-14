import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M, K = map(int,input().split()) #N은 집의 개수, M은 연속개수, K는 최소 경보울림
    List = list(map(int,input().split()))
    Sum = [0]*N
    k = 0
    ans = 0
    cnt = 0
    for i in range(N):
        k += List[i]
        Sum[i] = k
        if List[i] < K:
            cnt += 1
    if M == 1:
        print(cnt)
        continue
    elif M == N:
        if Sum[N-1] < K:
            print(1)
        else:
            print(0)
        continue
    for i in range(N):
        j = i-M
        if j == -1:
            value = Sum[i]
        elif j < -1:
            value = Sum[i]+Sum[N-1]-Sum[N+j]
        elif j >= 0:
            value = Sum[i]-Sum[j]
        if value < K:
            ans += 1
    print(ans)