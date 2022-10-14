import sys
input = sys.stdin.readline
left = list(input()[:-1])
right = list()
N = int(input())
for i in range(N):
    l = input()
    a = l[0]
    if a == 'P':
        left.append(l[2])
    elif a == 'B':
        if left:
            left.pop()
    elif a == 'D':
        if right:
            left.append(right.pop())
    elif a == 'L':
        if left:
            right.append(left.pop())
sys.stdout.write(''.join(left + right[::-1]))