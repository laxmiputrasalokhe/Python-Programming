x=int(input())
y=int(input())
m=min(x,y)
for i in range(1,m+1):
 if(x%i==0) and (y%i==0):
  hcf=i
z=(x*y)/hcf
print(z)
