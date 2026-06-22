import random
Words=["Apple", "Banana", "Laptop", "Sunset", "Guitar"]
Secret_Word= random.choice(Words).lower()
Guessed_Word= ["_"]*len(Secret_Word)
Attempts=6
print("--------Welcome To Hangman Game--------")
while Attempts>0 and "_" in Guessed_Word:
    print("Word: "+"".join(Guessed_Word))
    print("Attempts Left:", Attempts)
    User_Guess= input("Guess a Letter:").lower()
    if User_Guess in Secret_Word:
        print("Congratulations! You Have Successfully Guessed the Word.")
        for i in range(len(Secret_Word)):
            if Secret_Word[i]==User_Guess:
                Guessed_Word[i]= User_Guess
    else:
        print("Incorrect Guess!")
        Attempts-=1
if "_" not in Guessed_Word:
    print("--------You Won!--------\nCongratulations")
else:
    print("--------Game Over--------\nThe Guessed Word Was:", Secret_Word, ".")
