A = input()
from collections import deque
Str = deque(input())

left = []
right = []
while Str:
    while Str:
        left.append(Str.popleft())
        check = 0
        if left and left[-1] == A[-1] and len(left) >= len(A) and left[len(left)-len(A):] == list(A):
            k = len(A)
            while k > 0:
                left.pop()
                k -= 1
            check = 1
        if check == 1:
            break
    while Str:
        right.append(Str.pop())
        check = 0
        if right and right[-1] == A[0] and len(right) >= len(A) and right[len(right)-len(A):] == list(A)[::-1]:
            k = len(A)
            while k > 0:
                right.pop()
                k -= 1
            check = 1
        if check == 1:
            break

while left:
    right.append(left.pop())
    while right and right[-1] == A[0] and len(right) >= len(A) and right[len(right)-len(A):] == list(A)[::-1]:
            k = len(A)
            while k > 0:
                right.pop()
                k -= 1
print("".join(right[::-1]))