response = input("Press 1 to play the quiz or 2 to add new questions\n")

if response == '1':
    import quiz
elif response == '2':
    import add_questions
else:
    print "You did not choose a valid option"
