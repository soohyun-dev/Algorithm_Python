def fibonacci(num):
    arr=[1]*(num+1)
    for i in range(4,N+1):
        arr[i]=arr[i-1]+arr[i-3]
    return arr[num]

N=int(input())
print(fibonacci(N))