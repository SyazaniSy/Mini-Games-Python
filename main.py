import hangman, register
import os
f_team = [] # Create a list for storing team object

def main(): # Main Menu

    print("Welcome to the game! ")

    prompt = ''
    while(prompt != "Q" and prompt !='q'):
        print("Type 'H' for help")
        print("Type 'R' to register team & players")
        print("Type 'Q' to quit")
        print('*'*40)
        prompt = input("Please enter your command: ")
        if prompt == "GO":  # Option to start the game
            hangman.start(f_team)
        elif prompt == "H": # Option to get Help
            os.system("help.txt")
        elif prompt == "R" or prompt == "r": # Option to register team and players   
            print("Save the namelist.txt file and close it (●'◡'●)")
            os.system("namelist.txt")
            prompt = input("Press 'ENTER' after finish player registration: ")
            f_team = register.process_namelist()
            print("Type 'GO' to start the game")
    print("Thanks for playing, See yall")
    exit()


main()