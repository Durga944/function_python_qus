def drive():
    speed=int(input("enter any num"))
    if(speed<70):
        print("ok")
    if(speed>70):
        a=speed-70
        b=a//5
        if(b>12):
            print("liecense suspended",b)
        else:
            print(b)
drive()