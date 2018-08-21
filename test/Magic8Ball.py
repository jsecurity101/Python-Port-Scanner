# Import the modules
import sys
import random

ans = True

while ans:
    question = raw_input("Ask the magic 8 ball a question: (press enter to quit) ")

    answers = random.randint(1,8)

    if question == "":
        sys.exit()

    elif answers == 1:
        print "If this is what you want then yes"

    elif answers == 2:
        print "No Rookie"

    elif answers == 3:
        print "I dont speak spanish I am sorry"

    elif answers == 4:
        print "Do not bother me with a stupid question like that"

    elif answers == 5:
        print "Are you sure that is the question you would like to ask?"

    elif answers == 6:
        print "They it dont do what it do but it do"

    elif answers == 7:
        print "Yes"

    elif answers == 8:
        print "I am sorry but the answer is no"
