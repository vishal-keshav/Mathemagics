"""Author: bulletcross@gmail.com
   No copyright licenses"""

#Importing modules, slow but works
import random

"""Probability that we get a number
   greater than or equal to current one
   given that some number of throws are left
   
   @prama: n number currently holding
   @param: c number of throws left from now"""
def Q1(n,c):
    #Checkings
    if n>6 or n<1 or c<0:
        print("Incorrect usage of function")
        return float((-1))
    if c==0:
        return float(0)
    else:
        return (float(Q1(n,c-1))*float((n-1)/6.0) + float((7-n)/6.0))

"""Probability that we get a number
   greater than current one  given that
   some number of throws are left
   
   @prama: n number currently holding
   @param: c number of throws left from now"""
def Q2(n,c):
    #Checkings
    if n>6 or n<1 or c<0:
        print("Incorrect usage of function")
        return float((-1))
    if c==0:
        return float(0)
    else:
        return (float(Q2(n,c-1))*float((n)/6.0) + float((6-n)/6.0))


"""Using uniform float generator, return a dice face"""
def roll_a_dice():
    number = random.uniform(0, 6)
    if number <=1:
        return 1
    if number >1 and number <=2:
        return 2
    if number >2 and number <=3:
        return 3
    if number >3 and number <=4:
        return 4
    if number >4 and number <=5:
        return 5
    if number >5 and number <=6:
        return 6
"""At any stage of playing, decide wheather to go for one more chance"""
def play_more():
    number = random.uniform(0,1)
    if number <=0.5:
        return False
    if number >0.5:
        return True

"""This is for simulating scenarioe with left chances that
   if different choices are taken, then how many successes one can have
   By success, it is meant that we get a number greater that initial_number

   @param: initial_number number currently holding
   @param: chances_left how many throws are allowed
   @return: number of successe with given number of chances"""
def simulate_once(initial_number,chances_left):
    #Generate chances_left uniform numbers from 1 to 6 with probability 1/6
##    success = 0
##    #number_holding = initial_number
##    for i in range(0,chances_left):
##        face_number = roll_a_dice()
##        if face_number > initial_number:
##            success = success + 1
##    return success
    face_number = initial_number
    for i in range(0,chances_left):
        face_number = roll_a_dice()
        if face_number > initial_number:
            return 1
    return 0

#########################################################################################################

#Checking how uniform the random dice roll is
nr_rolls = 10000000
nr_number_observed = 0

for i in range(0,nr_rolls):
    if roll_a_dice() == 5:
        nr_number_observed = nr_number_observed + 1

#print(float(nr_number_observed)/float(nr_rolls))

#Simulation of probability of winning
first_throw_value = 5
throw_chances_left = 3

total_situation = 0
total_success_situation = 0

nr_simulation = 1000000
for i in range(0,nr_simulation):
    total_situation = total_situation + 1
    total_success_situation = total_success_situation + simulate_once(first_throw_value,throw_chances_left)
print("Using simulation")
print(float(total_success_situation)/float(total_situation))

#Using probability formulae for winning
print("Using probability theory")
print(Q2(first_throw_value,throw_chances_left))
###########################################################################################################
