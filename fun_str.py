def str():
    a=input("enter any num")
    b=input("enter any num")
    if(len(a)>len(b)):
        print(a,"it is big")
    elif(len(a)==len(b)):
        print(a)
        print(b)
    else:
        print("nothing")
str()