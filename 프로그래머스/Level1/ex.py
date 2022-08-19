arr=[1,2,3,4,5]
tree=[[0,0] for _ in range(5)]
for i in range(5):
    tree[i][0],tree[i][1]=arr[i]%2,arr[i]%2