import random

WordList = ["hello", "pink", "programming", "python"]
random.shuffle(WordList)
print("WordList after shufflled", WordList)

# list will make the word into individual letters
First_word = WordList[0]
answer = list(First_word)

print(answer)
print(First_word)

display = []

#new
used =[]
# ===========================15 mins==========================

# add independent vairables/letters into this display
display.append(answer)

#new
used.append(display)
# print(display)
# -----------hint----------------
for i in range(5):
    print(i)

print(len("pink"))
# --------------------------------

for i in range(len(display)):
    display[i] = "-"

# join to put space between each -
print(' '.join(display))
print()
# ===========================25 mins ==========================
# ===========================15 mins break==========================


# make a stopper
count = 0
incorrect = 5

# --------hint: how to use while-------
j = 0
while(j < 5):
    # j = j + 1
    j =+ 1
    print(j)

#--------hint: how to use input func-------
input("Please guess a letter: ")
# --------------------------------------------
# ===========================50 mins ==========================

# --------hint: how to use if-------
Variable_a = 1
if Variable_a ==1:
    print("True")
else:
    print("False")
# --------------------------------------------
# --------hint: how to use check-------
List_a = [1, 2, 3, 4]
if 1 in List_a:
    print("Yes")

List_a.remove(1)
print(List_a)
# --------------------------------------------

while count < len(answer) and incorrect > 0:
    guess = input("Please guess a letter: ")
    # convert the letter to a lower case
    # === 5-10 mins free coding lower func by google themselves
    guess = guess.lower()
    print(count)
# ===========================70 mins ==========================
# ===hint above====

    for i in range(len(answer)):
        if answer[i] == guess and guess in used:
            display[i] = guess
            count = count+1
            used.remove(guess)

    if guess not in display:
        incorrect = incorrect-1
        print("Sorry, Wrong guess")
    print("you have guessed:", count, "correct letters")
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


