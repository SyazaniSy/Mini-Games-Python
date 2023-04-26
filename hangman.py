##import modules
import random
import sum_it_up
import os


HANGMAN = ( #Tuple for the hangman graphics
"""
  Chance:6
  ----
  |   |
  |
  |
  |
  |
  |
------
""",
"""
  Chance:5
  ----
  |   |
  | (0
  |
  |
  |
  |
------
""",
"""
  Chance:4
  ----
  |   |
  | (0 0)
  |
  |
  |
  |
------
""",
"""
  Chance:3
  ----
  |   |
  | (0 0)
  | ( o )
  |
  |
  |
------
""",
"""
  Chance:2
  ----
  |   |
  | (0 0)
  | ( o )
  | |   |
  |
  |
------
""",
"""
  Chance:1
  ----
  |   |
  | (0 0)
  | ( o )
  | |---|
  |
  |
------
""",
"""
  Chance:0
  ----
  |   |
  | (0 0)
  | ( o )
  | |---|
  |  | |
  |
------
"""
)

def start(f_team): # Method to start the game
  os.system('cls')
  fin = open("hangman_word_list.txt","r")
  myfile = fin.readlines()
  fin.close()
  word_list = list()
  for word in myfile: # Create a list of words read from the file
      word_list.append(word.strip())

  rng = random.Random()
  word_random = rng.sample(word_list,2)

  print("Welcome to HANGMAN competition!!!")
  for team in f_team: # 
    print(team.team_name, "\nGet ready!!!")
    team.score = 0
    for i in range(2): # Play for 2 turns
        word_random = rng.choice(word_list)
        maximum_false = len(HANGMAN)
        until_now = "-" * len(word_random)
        false = 0
        used = []
        print("1,2,3,go!!!")

        while false < maximum_false and until_now != word_random: # While the word is not guessed

            guess = input("Enter your guess: ")
            used.append(guess)

            if guess in word_random:                               # If the guess is in the word
                new_word = ""
                for i in range(len(word_random)):
                    if guess == word_random[i]:
                        new_word += guess
                    elif guess != word_random[i]:
                        new_word += until_now[i]
                until_now = new_word

            else:                                                # If the guess is not in the word
                print("your guess, ",guess ,"is wrong (0_0!)")
                print(HANGMAN[false])
                false+=1

            print ("You've used the following letters: \n", used)
            print ("The word so far guessed is : ", until_now)

        if false == maximum_false: # If all the chances are used
            print("No chance left! 😥")
            print("The word is",word_random)
            team.score+=0
            print("Score :",team.score)

        else: # If the word is guessed
            print("Success! 😎")
            print("The word you guessed is ", word_random)
            team.score+=5
            print("Score :",team.score)
  input("Next game? (Press ENTER)")
  next_game(f_team)

def next_game(f_team): # Method to next module
  sum_it_up.start(f_team)

