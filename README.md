# Fun Maths Quiz!
## This is a simple multiplication quiz in python
### User Information:
This quiz is incredibly easy to use, simply run the code and you will be prompted with a multiplication question.
Enter your response within the terminal - if you are correct, you will be notified through the message: "That's correct, well done!"
Whereas if you are incorrect, you will be met with the message: "Not quite!"


### Technical Documentation:
This code primarily operates through 2 custom functions, "ask_question()" and "check_answer()".

Additonally, I have introduced a self contained module through the "questions.py" file which adds a layer of modularity to the code and is what is being used to provide us with random integers in the range of 1-10. Again, this file also uses a custom function "number_gen()". This function is linked with the main.py file by importing it in (as seen in line 2 of main.py).

The random library has also been imported to provide us with randomised integers.

The text that is displayed whether the answer will be correct or incorrect is managed through if/else statements. As for the question itself, that is simply a print statement which bakes in the randomised integers.


Users are able to input a figure after the question through the variable "user_input", which uses 2 built=in functions:


"input": this function allows the user to type something in, however stores the data as a string.


"int": this function is used to convert the string into an integer, which is required for this quiz since the program will not recognise the string as a possible answer, even if you enter the correct value.
