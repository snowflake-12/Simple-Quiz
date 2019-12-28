import sys
import difflib

def get_questions():
    with open('questions.txt') as f:
        lines = f.readlines()
    return [(lines[i], lines[i+1].strip()) for i in range(0, len(lines), 2)]


try:
    questions = get_questions()
except IOError as e:
    print ('Error reading questions file %s' % e)
    sys.exit()
except IndexError:
    print ('Error: all questions in the questions file must have answers.')
    sys.exit()

score = 0
total = len(questions)
for question, answer in questions:
    guesses = 1
    correct = 'no'

    while guesses < 4 and correct == 'no':
        guess = (question.strip() + ' (Guess %s)\n' % guesses)
        q = difflib.SequenceMatcher(None, guess, answer)
        if round(q.ratio(), 1) >= 0.6:
            score += 1
            correct = 'yes'
        guesses += 1


print ('You got %s out of %s questions right' % (score, total))
