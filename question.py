
import json


class Question:

    def __init__(self,id,text,answer,difficulty,options):
        self.id = id
        self.text = text
        self.answer = answer
        self.difficulty = difficulty
        self.options = options

    def display(self):
        return self.id,self.text,self.answer,self.difficulty,self.options




class Quiz:

    def __init__(self,name):
        self.name = name
        self.questions = []
        

    def addQuestion(self):
        id = input('enter the id')
        text = input("Enter the question text")
        while True:
            difficulty = input("Enter the difficulty:(easy/difficult)")
            if difficulty == 'easy' or difficulty == 'difficult':
                break
        print(text)
        options = [('a) '+ input('a:')),('b)'+ input('b:')),('c)'+input('c:')),('d)'+ input('d:'))]
        answer = input('What is the correct answer?(a,b,c,d)')
        question= Question(id,text,answer,difficulty,options)
        self.questions.append({'id': question.display()[0],'text':question.display()[1],'answer':question.display()[2],'difficulty':question.display()[3],'options':question.display()[4]})

    def save(self):
        with open('quizzes/{}.json'.format(self.name),'w') as f:
            json.dump(self.questions, f)

    def play(questions=[]):
        score = 0
        your_score = 0
        for i in range(len(questions)):
            print('Lets start to questions. You will be asked to enter the option you choose (a/b/c/d)','\n','Then your score will be calculated based on your answers and the difficulty of the questions.','\n',
            'Question {}: {}\noptions:\n{}\n{}\n{}\n{}'.format(i+1,questions[i]['text']),questions[i]['options'][0],questions[i]['options'][1],questions[i]['options'][2],questions[i]['options'][3])
            answ=input("Your answer:")
            if questions[i]['difficulty']=='easy':
                score+=5
                if answ==questions[i]['answer']:
                    your_score+=5
            elif questions[i]['difficulty']=='difficult':
                score+=10
                if answ==questions[i]['answer']:
                    your_score+=10
            print('Your score is {} out of {}'.format(your_score,score)) 
# quiz = Quiz('math')
# quiz.addQuestion()
