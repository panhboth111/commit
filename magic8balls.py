import random

def magic8Ball():
    print("Welcome to the Magic 8 Ball")
    x = input("What is your question my child?")
    answerList = ["It is certain",
                  "Outlook good",
                  "Hells yea",
                  "You may rely on it",
                  "Ask again later",
                  "Concentrate and ask again",
                  "Reply hazy, try again",
                  "My reply is no",
                  "Girl, things is looking tough",
                  "My sources say no"]
    randomAnswer = random.choice(answerList)

    if x == "":
        print("Please ask a question buddy!")
        exit()
    else:
        print(randomAnswer)
        askAgain()

def askAgain():
    x = input("Would you like to ask the Magic 8 Ball another question? Y/N")
    if x == "Y" or x == "y":
        magic8Ball()
    else:
        print("Thanks for visiting the Magic 8 Ball")
        exit()

magic8Ball()
