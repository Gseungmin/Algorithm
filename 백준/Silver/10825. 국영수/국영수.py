N = int(input())
List = []
for i in range(N):
    A, B, C, D = map(str,input().split())
    List.append([100-int(B),int(C),100-int(D),A])
List.sort()
for i in List:
    print(i[-1])