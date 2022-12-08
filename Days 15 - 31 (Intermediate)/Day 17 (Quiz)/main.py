from QuizBrain import Quiz

valid = ["True", "False"]
user_answer = ''

quiz = Quiz()

while quiz.play == True:
    quiz.question_answer()
    while user_answer not in valid:
        user_answer = input("True or False?   ").capitalize()
    quiz.check_answer(user_answer = user_answer)
    user_answer = ''