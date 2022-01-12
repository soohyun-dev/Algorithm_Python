pixel1, pixel2, bit = map(int, input().split())
store = (pixel1*pixel2*bit)/8/1024/1024
print('%.2f MB' %store)


