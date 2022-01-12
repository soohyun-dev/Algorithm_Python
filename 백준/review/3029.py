h1,m1,s1=map(int,input().split(':'))
h2,m2,s2=map(int,input().split(':'))
Time1=(h1*60*60)+(m1*60)+s1
Time2=(h2*60*60)+(m2*60)+s2
if(Time1>=Time2):
  result=((24*60*60)-Time1)+Time2
else:
  result=Time2-Time1
h=result//60//60
m=result//60%60
s=result%60
print("%02d:%02d:%02d" %(h,m,s))