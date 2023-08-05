#-----------------------------------------------------------
def new_game():
    guesses=[]
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter(A,B,C or D )")
        guess=guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses,guesses)

#-----------------------------------------------------------
def check_answer(answer,guess):
   if answer == guess:
       print("CORRECT")
       return 1
   else:
       print("INCORRECT")
       return 0 
   
#-----------------------------------------------------------

def display_score(correct_guesses,guesses):
    print("--------------------")
    print("RESULTS")
    print("--------------------")
    print("Answers :",end = " ")

    for i in questions:
        print(questions.get(i),end = " ")
    print()

    for i in guesses:
        print(i,end=" ")
    print()

    score = int(correct_guesses/len(questions)*100)
    print("Your Score is "+str(score)+"%")

#-----------------------------------------------------------
def play_again():
    response = input("Do you want to play again (yes/no):")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

questions = {
    "Who created python :" : "A",
    "In which year python was created  :":"B",
    "Python is tributed to which comedy group":"C",
    "Is Earth round :":"A"
}

options=[
    ["A. Guido Van Rossum","B. ELon Musk", "C. Mahatama Gandhi","D. Glenn Maxwell"],
    ["A.1981","B. 1991","C.1982","D. 1999"],
    ["A. Tarak Mehta ka ooltah Chasmah","B.Freinds","C.Monty Python","D. Vampire Diaries"],
    ["A. True","B.False","C. Maybe","D.what is earth ?"]
]
new_game()

while play_again():
    new_game()

print("Byeee!!")