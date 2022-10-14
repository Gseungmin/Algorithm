N = int(input())
A = list(input())

if N == 1:
    print(int(A[0]))
    exit()

check = []
ans = []

def reculsive(A, index, N, check, ans):
    if index >= N:
        B = []
        for i in A:
            if i == '+' or i == '*' or i == '-':
                B.append(i)
                continue
            B.append(int(i))
        for i in check:
            if B[i] == '+':
                B[i-1] = B[i-1]+B[i+1]
                B[i+1] = 'n'
                B[i] = 'n'
            if B[i] == '-':
                B[i-1] = B[i-1]-B[i+1]
                B[i+1] = 'n'
                B[i] = 'n'
            if B[i] == '*':
                B[i-1] = B[i-1]*B[i+1]
                B[i+1] = 'n'
                B[i] = 'n'
        for i in range(N):
            if B[i] == '*':
                pi = i+1
                mi = i-1
                while 1:
                    if B[pi] != 'n':
                        break
                    pi += 1
                while 1:
                    if B[mi] != 'n':
                        break
                    mi -= 1
                B[i] = 'n'
                B[mi] = B[pi] * B[mi]
                B[pi] = 'n'
        for i in range(N):
            if B[i] == '+' or B[i] == '-':
                pi = i+1
                mi = i-1
                while 1:
                    if B[pi] != 'n':
                        break
                    pi += 1
                while 1:
                    if B[mi] != 'n':
                        break
                    mi -= 1
                if B[i] == '+':
                    B[i] = 'n'
                    B[mi] = B[pi] + B[mi]
                    B[pi] = 'n'
                if B[i] == '-':
                    B[i] = 'n'
                    B[mi] = B[mi] - B[pi]
                    B[pi] = 'n'
        for i in B:
            if i != 'n':
                ans.append(i)
                break
        return
    if index-2 not in check:
        check.append(index)
        reculsive(A, index+2, N, check, ans)
        check.pop()
    reculsive(A, index+2, N, check, ans)
    return

reculsive(A, 1, N, check, ans)
print(max(ans))