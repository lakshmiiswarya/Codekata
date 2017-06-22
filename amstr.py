a=int(input("enter the number"))
temp=a
a1=str(a)
b=len(a1)
print(b)
sum=0
while temp!=0:
   digit = temp % 10
   q=temp//10
   temp=q
   sum += digit ** b
if a == sum:
   print(a,"is an Armstrong number")
else:
   print(a,"is not an Armstrong number")
