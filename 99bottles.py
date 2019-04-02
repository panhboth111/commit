def StandardVerse(n):
    print n, "bottles of beer on the wall,", n, ",bottles of beer"
    print "take one down pass it around,",n,"bottles of beer on the wall."

def TwoBottles():
    print "Two bottles of beer on the wall, two bottles of beer."
    print "Take one down pass it around, one bottle of beer on the wall."

def OneBottle():
    print "One bottle of beer on the wall, One bottle of beer."
    print "Take one down, pass it around, no more bottles of beer on the wall."

def NoBottles():
    print "No more bottles of beer on the wall, no more bottles of beer."
    print "Go to the store, buy some more, 99 bottles of beer on the wall."

for n in range(99,0,-1):
    if n > 2:
        StandardVerse(n)
    elif n == 2:
        TwoBottles()
    elif n == 1:
        OneBottle()
    else:
        NoBottles()
