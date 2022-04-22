B,C,D=map(int,input().split())
burger=sorted(list(map(int,input().split())), reverse=True)
side=sorted(list(map(int,input().split())), reverse=True)
drink=sorted(list(map(int,input().split())), reverse=True)

b_len=len(burger)
s_len=len(side)
d_len=len(drink)
cnt=min(b_len,s_len,d_len)

total=sum(burger)+sum(side)+sum(drink)
origin_price=total
set_price=0
for i in range(cnt):
    tmp=burger[i]+side[i]+drink[i]
    print(tmp)
    total-=tmp
    set_price+=int(tmp*0.9)

print(origin_price)
print(set_price+total)