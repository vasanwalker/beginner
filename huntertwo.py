def stair():
	s=0
	l=[]
	n=int(input())
	for i in range(n):
		l.append(int(input()))
	for i in l:
		s+=(n-i)
	print(s)
  
try:
  stair()
except:
  print('innvalid')
