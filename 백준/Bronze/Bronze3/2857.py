LIST=[]
for i in range(1,6):
    name=input()
    if 'FBI' in name:
        LIST.append(i)

if len(LIST)>0:
    print(*(LIST))
else:
    print('HE GOT AWAY!')