#The continue statement is used to skip the current block and move ahead to the next iteration, without executing the statements inside the loop.
#It can be used with both the while and for loops.
#Your task here is very special: you must design a vowel eater! Write a program that uses:
#a for loop;
#the concept of conditional execution (if-elif-else)
#the continue statement.
#Your program must:
#ask the user to enter a word;
#use user_word = user_word.upper() to convert the word entered by the user to upper case;
#use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
#print the uneaten letters to the screen, each one of them on a separate line.
#Test your program with the data we've provided for you.


# Prompt the user to enter a word and assign it to the user_word variable.
user_word=input("Enter a word: ")
user_word = user_word.upper()
n_letter=0
l=len(user_word)
for n_letter in range(l):
    if user_word[n_letter]=="A":
        continue
    elif user_word[n_letter]=="E":
        continue
    elif user_word[n_letter]=="I":
        continue
    elif user_word[n_letter]=="O":
        continue
    elif user_word[n_letter]=="U":
        continue
    else:
        print(user_word[n_letter])#, end="")