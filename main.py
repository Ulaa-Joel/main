import random

while True:
    print("Pick either: \n 1 for Rock \n 2 for Paper \n 3 for Scissors \n")
 
    player = int(input("Player turn: "))
    while player < 1 or player > 3:
        player = int(input("Enter valid choice: "))
    bet = ["rock", "paper", "scissors"]
    cpu = random.choice(bet)
    print("Computer picks " +cpu)

    if player == 1:
        choice = "rock"
    elif player == 2:
        choice = "paper"
    else:
        choice = "scissors"
    print("Player "+"("+choice+")"+ ": CPU "+"("+cpu+")")

    if choice == cpu:
        print("Draw")
    elif choice == "rock":
        if cpu == "scissors":
            print("rock smashes scissors! Player wins!")
            break
        else:
            print("Paper covers rock! Computer wins!")
            break
    elif choice == "paper":
        if cpu == "scissors":
            print("Scissors cuts paper! Computer wins!")
            break
        else:
            print("Paper covers rock! Player wins!")
            break
    elif choice == "scissors":
        if cpu == "rock":
            print("rock smashes scissors! Computer wins!")
            break
        else:
            print("Scissors cuts paper! Player wins!")
            break