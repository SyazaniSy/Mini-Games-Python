def sorting_result(f_team): # Method to sort the team object by score attributes
    f_team.sort(key=lambda x: x.score, reverse=True)
    ranking = {}
    for team in f_team: # Store the result in the format of team_name : score in dictonary
        ranking.update({team.team_name:team.score})   
    showing_result(ranking)

def showing_result(ranking):    # Method to show the result on the screen
    rank = list(ranking.items())    # Convert the dictionary to list
    print("TA-DA- 🥳")
    print("The ranking is:")
    for i in rank:  # Print the result
        print("{0} score: {1}".format(i[0], i[1]))
    write_to_file(rank)

def write_to_file(rank):    # Method to write the result to file
    f = open("ranking.txt", "w")
    for i in rank:
        w = str(i)  # Convert the tuple w to string
        f.write(w)
        f.write('\n')
    f.close()
    print("The result is successfully recorded in ranking.txt")
    print("The End of Game")