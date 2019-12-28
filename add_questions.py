def add_question():
    question = input('Type your question\n')
    write_to_file(question)



def add_answer():
    answer = input('Type your answer\n')
    write_to_file(answer)

def write_to_file(input):
    with open('questions.txt', 'a') as f:
        f.write('\n'+input)

check = True

while check == True:
    add_question()
    add_answer()
    if  input('Do you want to add another question?') == 'yes':
        check = True
    else: check = False
