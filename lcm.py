x=int(input())
y=int(input())
m=max(x,y)
for i in range(m,x*y+1):
 if(i%x==0) and (i%y==0):
  lcm=i
  break
print(lcm)

