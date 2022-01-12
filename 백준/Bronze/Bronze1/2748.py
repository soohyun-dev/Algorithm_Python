n=int(input())
s_num=0
n_num=1
for i in range(n):
  store=n_num
  n_num=s_num+n_num
  s_num=store
print(s_num)


