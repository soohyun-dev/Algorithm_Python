a,b=map(int,input().split())

result=0
boo=[]
nums=[]
for i in range(a,b+1):
    if i%2!=0:
        result+=i
        nums.append(i)
        boo.append('+')
    else:
        result-=i
        nums.append(i)
        boo.append('-')

for i in range(len(boo)):
    print(boo[i]+str(nums[i]),end='')
print('=%d' %(result))