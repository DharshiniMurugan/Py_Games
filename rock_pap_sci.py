import random
def play():
    user=input("'r' for rock 'p' for paper 's' for scissor: ")
    comp=random.choice(["r","p","s"])
    print(comp)
    if(user=="r" and comp=="p"):
        print(f"comp {comp} wins")
    elif(user=="p" and comp=="r"):
        print(f"user{user} wins")
    elif(user=="s" and comp =="p"):
        print(f"user{user} wins")
    elif (user == "s" and comp == "r"):
        print(f"comp {comp} wins")
    elif (user == "r" and comp == "s"):
        print(f"user{user} wins")
    elif (user == "p" and comp == "s"):
        print(f"comp {comp} wins")
    elif (user==comp):
        print("draw")
#play()
#======================================================================================
#======================================================================================

def lets_play():
    user = input("'r' for rock 'p' for paper 's' for scissor: ")
    comp = random.choice(["r", "p", "s"])
    print(comp)
    if (user==comp):
        print("draw")
    if iswin(user,comp):
        print("okay, you win")
    if iswin(comp,user):
        print("you lose")
def iswin(player,opponent):
    if((player=="r" and opponent=="s") or (player=="s" and opponent =="p") or(player=="p" and opponent=="r")):
        return True

lets_play()

