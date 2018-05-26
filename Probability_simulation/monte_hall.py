"""Author: bulletcross@gmail.com
   No copyright licenses"""
   
import random

"""Initialize game by putting a car in one door"""
def init_game():
    doors = ['goat','goat','goat']
    random_door = random.uniform(0,3)
    if random_door <=1:
        doors[0] = 'car'
        return doors
    elif random_door <=2:
        doors[1] = 'car'
        return doors
    else:
        doors[2] = 'car'
        return doors

"""Random chice made by palyer before any revelation"""
def first_choice():
    random_door = random.uniform(0,3)
    if random_door <=1:
        return 0
    elif random_door <=2:
        return 1
    else:
        return 2

"""Opening a door with a goat, other than players choice or a car in it"""
def show_a_goat(doors, first_choice):
    for i in range(0,3):
        if (i is first_choice) or (doors[i]=='car'):
            continue
        else:
            opened_door = i
            break
    return opened_door

"""Return 1 if won by switching, else 0
    @param: doors doors with a car and two goats
    @param: first_choice initial choice of player before a goat is reealed
    @param: opened_door door opened by presenter with a goat in it"""
def win_with_switch(doors,first_choice,opened_door):
    #opened door cannot be the first choice or a door with a car
    for i in range(0,3):
        if (i is first_choice) or (i is opened_door):
            continue
        else:
            other_door = i
            break
    if doors[other_door] == 'car':
        return 1
    else:
        return 0

###############################################################################

nr_games = 100000
nr_wins = 0

doors = init_game()
for i in range(0, nr_games):
    players_choice = first_choice()
    opened_door = show_a_goat(doors,first_choice)
    nr_wins = nr_wins + win_with_switch(doors,players_choice,opened_door)

print (nr_wins)
print float((float(nr_wins)/float(nr_games)))
###############################################################################
