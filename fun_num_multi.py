def num(limit):
    i=0
    sum=0
    while(i<limit):
        if(i%3==0 and i%5==0):
            print(i)
            sum= sum+i
        i=i+1
    print(sum)
num(100)
