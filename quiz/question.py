import json

class Question:
    def __init__(self, id, text, answer, difficulty, option):
        self.id = id
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
        self.options = ['a)'+option_a,'b)'+option_b,'c)'+option_c,'d)'+option_d]
        answer = input('What is the correct answer? (a/b/c/d) :')
        q1 = Question(text, answer, difficulty, self.options)
        self.question.appen({
                            "id": self.id,
                            "text":self.text,
                            "difficulty":self.difficulty,
                            "options":self.options,
                            "answer":self.answer
                            })


    def save(self):
        with open('quizzes/'+self.name+'.json', 'w') as jsFile:
            jsFile.write(json.dumps(self.question, indent=4))

    def play(self):
        point = 0
        for i in range(len(self.question)):
            print('''Let's start to questions. 
            You will be asked to enter the option you choose (a/b/c/d).
            Then your score will be calculated based on your answers and
            the difficlty of the questions.''')

            print(f'question{i+1} is {self.question["text"]}')
            print(f'''Options are:
                                {self.question[i]["option"][0]}\n
                                {self.question[i]["option"][1]}\n
                                {self.question[i]["option"][2]}\n
                                {self.question[i]["option"][3]}''')
            answer = input('enter your answer :')


q1 = Quiz()