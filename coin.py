def coinEstimator():

    ##########################################
    # Intro text                        ######
    ##########################################

    print("Welcome to the coin estimator.")
    print("Please enter the type of coins: ")
    print("1. Cent")
    print("2. Nickel")
    print("3. Dime")
    print("4. Quarter")


    ##############################################
    # Setting up variables for the user's input ##
    ##############################################

    userChoose = int(input("Enter: "))


    ##############################################################
    # Conditionals for different types of coin the user wants.  ##
    ##############################################################

    if userChoose == 1:             # Conditionals for Cents
        totalWeight = float(input("What is the total weight of your cents in grams?\n"))

        (cointValue, dimeWrapper) = cointEstSol(totalWeight, "Cent")

        print("The total cents you have is {0}. You need {1} wrapper(s)".format(cointValue, dimeWrapper))

    elif userChoose == 2:           # Conditionals for Nickel
        totalWeight = float(input("What is the total weight of your nickels in grams?\n"))

        (cointValue, dimeWrapper) = cointEstSol(totalWeight, "Nickel")

        print("The total nickels you have is {0}. You need {1} wrapper(s)".format(cointValue, dimeWrapper))

    elif userChoose == 3:           # Conditionals for Dime
        totalWeight = float(input("What is the total weight of your dimes in grams?\n"))

        (cointValue, dimeWrapper) = cointEstSol(totalWeight, "Dime")

        print("The total dimes you have is {0}. You need {1} wrapper(s)".format(cointValue, dimeWrapper))

    elif userChoose == 4:           # Conditionals for Quarter
        totalWeight = float(input("What is the total weight of your quarters in grams?\n"))

        (cointValue, dimeWrapper) = cointEstSol(totalWeight, "Quarter")

        print("The total quarters you have is {0}. You need {1} wrapper(s)".format(cointValue, dimeWrapper))


def cointEstSol(weight, coins):

    ########################################################
    ## Setting up variables for the solution of coins    ###
    ########################################################

    coinWeight = {"Cent": 126, "Nickel": 199, "Dime": 113, "Quarter": 226}     # Dictionary for the different weights of coins
    coinCountWrap = {"Cent": 50, "Nickel": 40, "Dime": 50, "Quarter": 40}      # Dictionary for the amount of coins that can be put in a wrapper

    cointValue = weight // coinWeight[coins]                                   # Solution to compute how many coins we have

    if cointValue < coinCountWrap[coins]:                                      # Conditionals for how many wrappers would be needed.
        coinWrapper = 1
    else:
        coinWrapper = cointValue // 50
        coinWrapper += 1

    return (cointValue, coinWrapper)                                           # Returning the total amount of coins and wrapper

coinEstimator()
