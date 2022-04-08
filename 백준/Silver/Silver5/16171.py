sample=list(input())
find=str(input())
cnt=0
newSample=''.join([i for i in sample if not i.isdigit()])
if find in newSample:
    print(1)
else:
    print(0)

    