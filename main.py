import random     # imports the random library
from questions import number_gen

def ask_question():
    num1, num2 = number_gen()
    print("What is ",num1,"*",num2,"?")
    return num1, num2


def check_answer(user_input,answer):
   if user_input == answer:
    print ("That's correct, well done!")
   else:
    print ("Not quite!")


num1, num2 = ask_question()
user_input = int(input(" "))
answer = num1*num2
check_answer(user_input, answer)