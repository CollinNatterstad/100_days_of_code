import random
'''#step 1 of hang man challenge
#choose a word at random. Guess a letter and see if that letter is in the word. 

#Create list of words
word_list = ["ardvark", "baboon", "zebra"]

#choose random word from list
word = random.choice(word_list).lower()
#ask the user to guess a letter and assign their answer to a variable called guess. make guess lowercase.

guess = input("Choose a Letter\n").lower()

for letter in word:
    if letter == guess:
        print('match')
    else:
        print('not match')
'''

'''#Step 2 of hangman challenge. 
#create a list of blanks that are modified when the correct solution is provided. 
word_list = ["ardvark", "baboon", "zebra"]

#choose random word from list
word = random.choice(word_list).lower()

word_list = []
blanks = []

for letter in word:
    word_list.append(letter)
    blanks += '_'

print(word_list)
print(blanks)

guess = input("Choose a Letter\n").lower()
#ask the user to guess a letter and assign their answer to a variable called guess. make guess lowercase.

for index, letter in enumerate(word):
    if letter == guess:
        blanks[index] = guess

print(word_list)
print(blanks)

#step 3 of hangman
#create a while loop that allows the users to guess until the word is correct

word_list = ["ardvark", "baboon", "zebra"]

#choose random word from list
word = random.choice(word_list).lower()

word_list = []
blanks = []

for letter in word:
    word_list.append(letter)
    blanks += '_'

#word_list included for testing purposes.
print(word_list)
print(blanks)

#ask the user to guess a letter and assign their answer to a variable called guess. make guess lowercase.
while word_list != blanks:
    guess = input("Choose a Letter\n").lower()
    for index, letter in enumerate(word):
        if letter == guess:
            blanks[index] = guess
    print(word_list)
    print(blanks)'''

# Step 4
# create a new variable that tracks lives in the game. Incorrect answers subtract 1
# game ends with lives == 0 OR word_list == blanks 

lives = 6 

word_list = ["ardvark", "baboon", "zebra"]

#choose random word from list
word = random.choice(word_list).lower()

word_list = []
blanks = []

for letter in word:
    word_list.append(letter)
    blanks += '_'

print(blanks)
miss = 0

#ask the user to guess a letter and assign their answer to a variable called guess. make guess lowercase.
while word_list != blanks and lives > 0:
    guess = input("Choose a Letter\n").lower()

    # this block of codes seeks letter AT an index. 
    # it will compare each letter in the list to the guessed letter itself    
    for index, letter in enumerate(word):
        if letter == guess:
            blanks[index] = guess

    #this block of code is looking at the guessed letter and seeing if it is in the word_list.
    #if it isn't, it will subtract one life and add one miss to the board (misses will be used to track a list index for the hang man character. )
    if guess not in word_list:
        lives -= 1
        miss += 1
        if lives > 0:
            print(f"You have {lives} remaining.")
        else:
            print("You lose.")

    print(blanks)

if word_list == blanks:
    print(blanks)
    print("You Win!")