# def outer(a,b):
#     def inner(n1,n2):
#         var=a+b
#         return(var)
#     return(inner(2,3))

print(outer(2,1))def change(list1,list2):
    i=0
    new=[] 
    sum=0
    while(i<len(list1)):
        sum= list1[i]*list2[i]
        new.append(sum)
        i=i+1
    print(new)
change([5, 10, 50, 20], [2, 20, 3, 5]) 