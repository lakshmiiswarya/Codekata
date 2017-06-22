a=int(input("enter the starting number"))
c=int(input("enter the ending number"))
for j in range(a,c):
 temp=j
 a1=str(j)
 b=len(a1)
 print(b)
 sum=0
  while temp!=0:
   digit = temp % 10
   q=temp//10
   temp=q
   sum += digit ** b
 if j == sum:
   print(j,"is an Armstrong number")
 else:
   print(j,"is not an Armstrong number")
