def armstrong():
    num = int(input("Enter a number: "))
    sum = 0
    a = num
    while a > 0:
        b = a% 10
        sum += b ** 3
        a //=10
    if num == sum:
        print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong number")
armstrong()
