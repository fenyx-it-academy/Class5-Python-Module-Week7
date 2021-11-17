import json

class Question:
    def __init__(self,text, answer, difficulty, option):
        self.text = text
        self.answer = answer
        self.difficulty = difficulty
        self.option = option


class Quiz:

    def __init__(self, name):
        self.name = name
        self.question = {}

    def addQuestion(self, id):
        text = input('enter your question : ')
        self.id = id
        self.id = 0
        while True:
            difficulty = input('What is the difficulty of the question? (easy/difficult) : ')
            if difficulty == 'easy' or difficulty == 'difficult':
                break
            else:
                print('e for "easy" or d for "difficult"')
                continue

        print('Please enter the options :')
        option_a = input('(a) ')
        option_b = input('(b) ')
        option_c = input('(c) ')
        option_d = input('(d) ')
        options = ['a)'+option_a,'b)'+option_b,'c)'+option_c,'d)'+option_d]
        answer = input('What is the correct answer? (a/b/c/d) :')
        q1 = Question(text, answer, difficulty,options)
        self.id += 1
        self.question["id"] = self.id
        self.question["text"] = text
        self.question["difficulty"] = difficulty
        self.question["options"] = options
        self.question["answer"] = answer



    def save(self):
        with open('quizzes/'+self.name+'.json', 'w') as jsFile:
            jsFile.write(json.dumps(self.question, indent=4))

    def play(self):
        point = 0
        score = 0
        for i in range(len(self.question)):
            print('''Let's start to questions. 
            You will be asked to enter the option you choose (a/b/c/d).
            Then your score will be calculated based on your answers and
            the difficlty of the questions.''')

            print(f'question{i+1} is {self.question["text"]}')
            print(f'''Options are:
                                {self.question[i]["option"][0]}
                                {self.question[i]["option"][1]}
                                {self.question[i]["option"][2]}
                                {self.question[i]["option"][3]}''')
            answer = input('enter your answer :')
            if answer == self.question[i]["answer"]:
                if self.question[i]["difficulty"] == 'easy':
                    point+=5
                    score+=5
                else:
                    point+=10
                    score+=10
            else:
                if self.question[i]["difficulty"] == 'easy':
                    score+=5
                else:
                    score+=10
        print(f'Your score is {point} out of {score}')

