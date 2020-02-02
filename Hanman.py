import random

WordList = ['hello', "pink" ,"programming", "python"]
random.shuffle(WordList)

# list will make the word into individual letters
answer = list(WordList[0])

# print(WordList[0])
# print(answer)

display = []

#new
used =[]
# add independent vairables/letters into this display
display.extend(answer)

#new
used.extend(display)
print(display)

for i in range(len(display)):
    display[i]="-"

# join to put space between each -
print(' '.join(display))
print()
# make a stopper
count = 0
incorrect = 5

while count < len(answer) and incorrect >0:
    guess = input("Please guess a letter: ")
    # convert the letter to a lower case
    guess = guess.lower()
    print(count)

    for i in range(len(answer)):
        if answer[i] == guess and guess in used:
            display[i] = guess
            count = count+1

            used.remove(guess)

    if guess not in display:
        incorrect = incorrect-1
        print("Sorry, Wrong guess")
    print("you have guessd:", count, "correct letters")
    print("you have", incorrect, "chances left")

    print(' '.join(display))
    print()


if count == len(answer):
    print("******************************")
    print("Congratulations, well done!")
    print("******************************")

else:
    print("------------------------------------")
    print("unfortunately, you run out of goes.")
    print("------------------------------------")


