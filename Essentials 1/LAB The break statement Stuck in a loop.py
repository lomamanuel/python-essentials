#The break statement is used to exit/terminate a loop.
#Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.
#Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement.

word=input("Insert a word or 'chupacabra' to exit: ")
while word!="chupacabra":
    if word=="chupacabra": break
    else:
        word=input("Insert a word or 'chupacabra' to exit: ")
print("You've successfully left the loop.")
