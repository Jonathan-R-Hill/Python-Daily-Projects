import requests


class Questions:
    def __init__(self):
        self.api = "https://opentdb.com/api.php?amount=10&type=boolean"
        self.response = requests.get(self.api)
        self.results = self.response.json()['results']
        self.question_list = []
        self.data = {}

        self.question_num = 0
        self.question = ''
        self.answer = ''

    def store_question_ans(self):
        for i in self.results:
            self.question_list.append(i)

        num = 1
        for index in self.question_list:
            self.data[num] = {}
            self.data[num]["question"] = index["question"]
            self.data[num]["correct_answer"] = index["correct_answer"]
            num += 1

        # strip &quot;   #039;
        strip_list = ['&quot;', "#039;", "&"]

        for i in range(1, len(self.data)):
            for strip in strip_list:
                self.data[i]['question'] = self.data[i]['question'].replace(strip, '')

    def update_question(self):
        if self.question_num < 10:
            self.question_num += 1
            self.question = self.data[self.question_num]['question']
            self.answer = self.data[self.question_num]['correct_answer']
        else:
            self.question = "End of Quiz. Click again"
