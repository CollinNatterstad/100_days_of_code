import random, english_words as ew
from OHDC_7_Hang_man_additionals import logo, stages, word_list



print(logo)
print("Welcome to Hangman!")
print("A random word will be selected from the dictionary.\nCan you guess what it is in six tries?")

lives = 6 

word_list = word_list

#choose random word from list
word = random.choice(word_list).lower()

word_list_game = []
blanks = []

for letter in word:
    word_list_game.append(letter)
    blanks += '_'

print(blanks)
miss = 0

#ask the user to guess a letter and assign their answer to a variable called guess. make guess lowercase.
while word_list_game != blanks and lives > 0:
    guess = input("Choose a Letter\n").lower()

    # this block of codes seeks letter AT an index. 
    # it will compare each letter in the list to the guessed letter itself    
    for index, letter in enumerate(word):
        if letter == guess:
            blanks[index] = guess

    #this block of code is looking at the guessed letter and seeing if it is in the word_list.
    #if it isn't, it will subtract one life and add one miss to the board (misses will be used to track a list index for the hang man character. )
    if guess not in word_list_game:
        lives -= 1
        if lives > 0:
            print(stages[lives])
            print(f"You have {lives} remaining.")
        else:
            print("You lose.")

    print(blanks)

if word_list_game == blanks:
    print(blanks)
    print("You Win!")