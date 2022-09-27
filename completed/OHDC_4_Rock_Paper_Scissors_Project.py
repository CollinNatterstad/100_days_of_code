
import random

selection = int(input("Would you like to choose rock, paper, or scissors? Type 0 for rock, 1 for paper, or 2 for scissors\n"))

outcomes = ['rock','paper','scissors']

index = random.randint(0,len(outcomes)-1)


if selection == 0 and index == 2:
    print("You Chose Rock")
    print("The Computer Chose Scissors")
    print("You Win!")
elif selection ==0 and index==1:
    print("You Chose Rock")
    print("The Computer Chose Paper")
    print("You Lose!")
elif selection ==0 and index== 0:
    print("You Chose Rock")
    print("The Computer Chose Rock")
    print("You Tie!")

if selection == 1 and index == 0:
    print("You Chose Paper")
    print("The Computer Chose Rock")
    print("You Win!")
elif selection ==1 and index==2:
    print("You Chose Paper")
    print("The Computer Chose Scissors")
    print("You Lose!")
elif selection ==1 and index==1:
    print("You Chose Paper")
    print("The Computer Chose Paper")
    print("You Tie!")

if selection == 2 and index == 1:
    print("You Chose Scissors")
    print("The Computer Chose Paper")
    print("You Win!")
elif selection == 2 and index==0:
    print("You Chose Scissors")
    print("The Computer Chose Rock")
    print("You Lose!")
elif selection == 2 and index==2:
    print("You Chose Scissors")
    print("The Computer Chose Scissors")
    print("You Tie!")