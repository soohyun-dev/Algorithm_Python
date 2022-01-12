num1=int(input())
num2=int(input())
a=num2//100
b=(num2-(a*100))//10
c=num2%10
print("%d\n%d\n%d\n%d" %(num1*c,num1*b,num1*a,num1*num2))