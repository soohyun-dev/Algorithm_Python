check=[None, True, False, True, True]
N=int(input())
for i in range(5, N):
    if check[i-4]!=check[i-3]!=check[i-1]:
        check.append(True)
    else:
        check.append(False)

if check[-1]==True:
    print('SK')
else:
    print('CY')