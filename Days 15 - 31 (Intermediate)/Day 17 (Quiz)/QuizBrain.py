from Data import question_data

class Quiz:
    
    def __init__(self):
        self.play = True
        self.question = ''
        self.answer = ''
        self.question_number = 0
        self.user_answer = ''
        self.score = 0
        
    def question_answer(self):
        self.question = question_data[self.question_number]["text"]
        self.answer = question_data[self.question_number]["answer"]
        self.question_number += 1
        
        print(f"{self.question_number}) {self.question}\n")
    
    def check_answer(self, user_answer):
        if (user_answer == self.answer):
            self.score += 1
            print(f"That is correct!")
    
        else:
            print(f"That is incorrect! the answer was {self.answer}")

            
        print(f"Your score is: {self.score}\n")
        
        if self.question_number == len(question_data):
            print(f"you have finished the quiz! Your score was: {self.score}!")
            self.play = False
        
        