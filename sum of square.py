a=int(input())
print(a)
c=0
d=a
while(d>0):
  b=d%10
  c+=b*b
  d=d//10
print (c)
