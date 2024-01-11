import random
import figures


username = input("What's your name?\n")

while True:
    print("")
    print(("Choose: "))  
    print("1 - Rock") 
    print("2 - Paper")
    print("3 - Scissor")
    print("4 - Quit")
    choice = int(input("Please insert your choice.\n"))
    computer = random.randint(1, 3)
    

    match choice:

        case 1:
            print("")
            print(f"{username}:\n{figures.Rock()}")
            if computer == 1:
                print("")
                print(f"Computer:\n{figures.Rock()}")
                print("")
                print("It's a draw")
            elif computer == 2:
                print("")
                print(f"Computer:\n{figures.Paper()}")
                print("")
                print(f"{username} you loose!!!")
            elif computer == 3:
                print("")
                print(f"Computer:\n{figures.Scissor()}")
                print("")
                print(f"{username} you win!!!")
            
        case 2:
            print("")
            print(f"{username}:\n{figures.Paper()}")
            if computer == 1:
                print("")
                print(f"Computer:\n{figures.Rock()}")
                print("")
                print(f"{username} you win!!!")
            elif computer == 2:
                print("")
                print(f"Computer:\n{figures.Paper()}")
                print("")
                print("It's a draw")
            elif computer == 3:
                print("")
                print(f"Computer:\n{figures.Scissor()}")
                print("")
                print(f"{username} you loose!!!")
            
        case 3:
            print("")
            print(f"{username}:\n{figures.Scissor()}")
            if computer == 1:
                print("")
                print(f"Computer:\n{figures.Rock()}")
                print("")
                print(f"{username} you loose!!!")
            elif computer == 2:
                print("")
                print(f"Computer:\n{figures.Paper()}")
                print("")
                print(f"{username} you win!!!")
            elif computer == 3:
                print("")
                print(f"Computer:\n{figures.Scissor()}")
                print("")
                print("It's a draw")
        
        case 4:
            print("")
            print("Thank you for playing..see you soon!!!")
            break

    

          

    