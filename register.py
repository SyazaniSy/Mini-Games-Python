class team():       # Create a new class called team
    def __init__(self, team_name, names, score = 0):
        self.team_name = team_name
        self.players = list(names)
        self.score = score

    def __str__(self):
        return ("{0} {1} \nScore: {2}\n".format(self.team_name, self.players, self.score))

def process_namelist():  # Method to process the namelist.txt file
    f = open("namelist.txt")
    content = f.read()
    f.close()

    teamlist = content.split(sep="\n\n")        # Split the content into a list of strings
    for i in range(len(teamlist)):      # Loop through the list of strings
        teamlist[i] = teamlist[i].split(sep="\n")       # Split players in each team into a list of strings
    return(display_teamlist(teamlist))

def display_teamlist(teamlist): # Method to display the teamlist
    for i in range(len(teamlist[0])):   # Loop through teamlist to print each team in a table
        if len(teamlist) == 1:
            layout = "{0:<20}"
            print(layout.format(teamlist[0][i], end="\n\n"))
        elif len(teamlist) == 2:
            layout = "{0:<20} {1:<20}"
            print(layout.format(teamlist[0][i],teamlist[1][i], end="\n\n"))
        elif len(teamlist) == 3:
            layout = "{0:<20} {1:<20} {2:<20}"
            print(layout.format(teamlist[0][i],teamlist[1][i],teamlist[2][i], end="\n\n"))
        elif len(teamlist) == 4:
            layout = "{0:<20} {1:<20} {2:<20} {3:<20}"
            print(layout.format(teamlist[0][i],teamlist[1][i],teamlist[2][i],teamlist[3][i], end="\n\n"))
    print("There are {0} teams in the file.".format(len(teamlist)))
    input("Press 'Enter' to confirm team setup 😊\n")
    return(create_team_obj(teamlist))
    

def create_team_obj(teamlist): # Method to create team objects
    f_team = list()
    for i in range(len(teamlist)):
        team_name = teamlist[i][0]  # Assign the team name
        players = teamlist[i][1:5]  # Assign the players 

        teams = team(team_name, players, 0)
        f_team.append(teams)
        print(f_team[i])
    print("Team object list created successfully\n")
    return (f_team) # Return the team object list to main.py

