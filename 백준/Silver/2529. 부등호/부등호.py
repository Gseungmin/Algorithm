import sys
input = sys.stdin.readline
N = int(input())
A = [0] + list(map(str,input().split()))
check = [0]*10
ans = []
def ok(N, index, A, ans):
    true = 0
    if A[index] == "<":
        if ans[index-1] < ans[index]:
            true = 1
    else:
        if ans[index-1] > ans[index]:
            true = 1
    return true
    
check_2 = [0]*10
ans_2 = []
def Max(N, index, A, check, ans):
    if index == N+1:
        return
    for k in range(9,-1,-1):
        if index == 0:
            ans.append(k)
            check[k] = 1 #use
            Max(N, index+1, A, check, ans)
            if len(ans) == N+1:
                return
            else:
                check[k] = 0 #not use
                ans.pop(-1)
        else:
            if check[k] == 0: #not use
                ans.append(k)
                true = ok(N, index, A, ans)
                if true == 1:
                    check[k] = 1 #use
                    Max(N, index+1, A, check, ans)
                    if len(ans) == N+1:
                        return
                    else:
                        check[k] = 0 #not use
                ans.pop(-1)
    return
Max(N, 0, A, check_2, ans_2)
print("".join(map(str,ans_2)))

def Min(N, index, A, check, ans):
    if index == N+1:
        return
    for k in range(10):
        if index == 0:
            ans.append(k)
            check[k] = 1 #use
            Min(N, index+1, A, check, ans)
            if len(ans) == N+1:
                return
            else:
                check[k] = 0 #not use
                ans.pop(-1)
        else:
            if check[k] == 0: #not use
                ans.append(k)
                true = ok(N, index, A, ans)
                if true == 1:
                    check[k] = 1 #use
                    Min(N, index+1, A, check, ans)
                    if len(ans) == N+1:
                        return
                    else:
                        check[k] = 0 #not use
                ans.pop(-1)
    return

Min(N, 0, A, check, ans)
print("".join(map(str,ans)))