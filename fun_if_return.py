def get_capital():
    country=input("enter any num")
    if(country=="india"):
        return("new delhi")
    elif(country=="france"):
        return("paris")
    elif(country=="uk"):
        return("londan")
    else:
        return("none")
print(get_capital())