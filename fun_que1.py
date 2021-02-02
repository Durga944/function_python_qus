def eligible_for_vote():
    age=int(input("enter any num"))
    if(age>=18):
        print("you are eligible")
    elif(age<18):
        print("not eligible")
eligible_for_vote()