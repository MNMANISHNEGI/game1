import random
def check(user,comp):
    if(comp== user):
        return 0
    if(comp==1 and user==3):
        return 1
    if (comp == 2 and user == 1):
        return 1
    if (comp == 3 and user == 2):
        return 1
    return 2

user=int(input("enter your choice 1 for stone ,2 for paper,3 for scissor \n"))
comp=random.randint(0,2)
score=check(user,comp)
if(score==0):
    print("the match is tied")
elif score==1:
    print("you loose")
else:
    print("you won")