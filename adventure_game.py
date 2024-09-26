name = input("Enter your name: ")
print("Hello " + name + ".")

do_you_want_to_play = input("Do you want to play? (y/n) ")
if do_you_want_to_play == "y":
    print("Welcome to the game.")
    c1 = input("Where do you want to go? (right/left) ")

    if c1 == "right":
        print("Okay! You have moved 1 unit towards the right direction.")
        weapon_1 = input("Choose a weapon: Axe or Sword. (axe/sword) ").lower()
        if weapon_1 == "axe":
            rfc1 = input("Do you want to cut a tree? (y/n) ")
            if rfc1 == "n":
                print("Congratulations! You won the game.")
            elif rfc1 == "y":
                print("You lose.")
            else:
                print("Invalid move.")
        elif weapon_1 == "sword":
            rfc2 = input("Do you want to kill someone? (y/n) ")
            if rfc2 == "y":
                print("Congratulations! You won the game.")
            elif rfc2 == "n":
                print("You lose.")
            else:
                print("Invalid move.")
        else:
            print("Invalid move.")

    elif c1 == "left":
        print("Okay! You have moved 1 unit towards the left direction.")
        weapon_2 = input("Choose a weapon: Axe or Sword. (axe/sword) ").lower()
        if weapon_2 == "axe":
            lfc1 = input("Do you want to cut the tree? (y/n) ")
            if lfc1 == "y":
                print("You won the game.")
            elif lfc1 == "n":
                print("You lose.")
            else:
                print("Invalid move.")
        elif weapon_2 == "sword":
            lfc2 = input("Do you want to kill someone? (y/n) ")
            if lfc2 == "y":
                print("You lose.")
            elif lfc2 == "n":
                print("You won.")
            else:
                print("Invalid move.")
        else:
            print("Invalid move.")

    else:
        print("Invalid move.")

elif do_you_want_to_play == "n":
    print("Maybe next time!")
else:
    print("Invalid input.")
