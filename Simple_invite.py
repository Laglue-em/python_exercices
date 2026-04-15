more="y"
total=0
while more=="y":
    name=input("What is the name of the person you want to invite to your party: ").capitalize()
    invitation=print(f"{name} has now been invited")
    total=total+1
    more= input("Do you want to invite somebody else:(y/n)")
print(f"You have {total}, people coming to your party." )
