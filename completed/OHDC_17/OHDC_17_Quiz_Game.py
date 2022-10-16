from OHDC_17_data import question_data
#ordinarily this would be in a different file. For convenience it is continued here. 
class Question:

    def __init__(self,question,answer):
        self.question = question
        self.answer = answer

#ordinarily this would be in a different file. For convenience it is continued here.
class QuizBrain:

    def __init__(self,question_bank):
        self.score = 0
        self.question_number = 0
        self.question_bank = question_bank

    def next_question(self):
        current_question = self.question_bank[self.question_number]

        self.question_number +=1
        user_choice = input(f'Q.{self.question_number}: {current_question.question}: (True/False)?\n').lower()
        self.check_answer(current_question.answer, user_choice)

    def still_has_question(self):
        #returns TRUE or FALSE depending on if the answer is correct.
        #Same as saying if else but with less writing.  
        return len(self.question_bank) > self.question_number 
    
    def keep_score(self,correct):
        if correct:
            self.score +=1
        else:
            pass

    def check_answer(self,current_answer, user_answer):
        
        if current_answer.lower() == user_answer:
            print("Correct!")
            correct = True

        elif current_answer.lower() != user_answer:
            print("Sorry, that's not correct.")
            correct = False
        
        self.keep_score(correct)

        print(f"The correct answer was: {current_answer}")
        print(f"Your current Score is: {self.score}/{self.question_number}")
        print('\n')

question_bank = []

for items in question_data:
    question = items['text']
    answer = items['answer']

    question_bank.append(Question(question=question,answer=answer))

quiz = QuizBrain(question_bank=question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")