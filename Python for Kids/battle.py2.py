import sys

#
# set up life
#

rarity_life = 10
discord_life = 20

#
# function - battle
#

def battle(rarity_life, discord_life, choice):

    choice = choice[:1]

    print("You picked %s" % choice)
    
    #Rarity hits discord
    if choice == "a":
        discord_life = discord_life - 1

    #Discord hits Rarity
    if choice == "b":
        rarity_life = rarity_life - 1

    #Discord takes her horn
    if choice == "c":
        rarity_life = rarity_life - 2

    #Nothing
    if choice == 'd':
        print("Do nothing, huh?")
        discord_life = discord_life - 0

    return rarity_life, discord_life


#
# main loop
# keep going while both are alive
#

while rarity_life >= 0 and discord_life >= 0:

    #
    # ask what happened
    #

    print("a=Rarity hits Discord   b=Discord hits Rarity  c=Discord takes her horn   d=nothing")
    what_happened = sys.stdin.readline()
    rarity_life, discord_life = battle(rarity_life, discord_life, what_happened)
    print("Rarity %s, Discord %s" % (rarity_life, discord_life))
    

