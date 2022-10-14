import sys
input = sys.stdin.readline
N=int(input())
s1=set()
result=0
s1.add(N)
while 1 not in s1:
	result+=1
	s2=s1.copy()
	for i in s2:
		if i%3==0:
			s1.add(i//3)
		if i%2==0:
			s1.add(i//2)
		s1.add(i-1)
	s1=s1-s2
print(result)