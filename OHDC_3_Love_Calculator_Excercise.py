print('welcome to the love calculator!')

#taking a supplied name
name1 = 'Angela Weberino'
name2 = 'Jonathon Cross'

#variables to iterate over
true = 'true'
love = 'love'

#baseline variable value
true_score = 0
love_score = 0 

#converting all letters to lowercase
names = name1.lower()+name2.lower()

#for loop to iterate over letters in true adds to score
for letter in true:
   true_score += names.count(letter)

#for loop to iterate over letters in love adds to score
for letter in love:
    love_score += names.count(letter)

#two scores are combined to make a 'total score' -> ts = 6 ls = 8 -> 68 not 14. convert to string for concatenation
combined = str(true_score)+str(love_score)

#convert back to int for if conditions
score = int(combined)

if score <= 10 or score >= 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif score >=40 and score <= 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'your score is {score}')