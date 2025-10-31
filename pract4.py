def funu(a):
    uni=[]
    
    for i in a:
        if i not in uni:
            uni.append(i)
    return uni
a=[1,3,2,3,4,5,2,3,7,8,12]
ab=funu(a)
print(ab)
