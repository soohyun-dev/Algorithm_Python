N=int(input())
dict={}
for i in range(N):
    n=int(input())
    try:
        dict[n]+=1
    except:
        dict[n]=1


result=sorted(dict.items(),key=lambda x:(-x[1],x[0]))
print(result[0][0])
