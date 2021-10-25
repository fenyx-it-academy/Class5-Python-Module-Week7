import json
class Question:
    def __init__(self,text,answer,difficulty,options):
        self.text=text
        self.answer=answer
        self.difficulty=difficulty
        self.options=options
    def __str__(self):
        return self.text,self.answer,self.difficulty,self.options

class Quiz:
    def __init__(self,name):
        self.name=name
        self.questions=[]
    def addQuestion(self,id):
        self.id=id
        text=input("Please enter the question: What is ... ? ")
        difficulty=input("easy or difficult: ")
        options=[("a) "+input("a: ")),("b) "+input("b: ")),("c) "+input("c: ")),("d) "+input("d: "))]
        answer=input("Answer(a,b,c,d): ")
        question=Question(text,answer,difficulty,options)
        self.questions.append({'id':self.id,'text':question.__str__()[0],'answer':question.__str__()[1],'difficulty':question.__str__()[2],
        'options':question.__str__()[3]})
    def save(self):
        with open("quizzes/{}.json".format(self.name),'w') as file:
            json.dump(self.questions,file)
    def play(questions=[]):
        score=0
        your_score=0
        for i in range(len(questions)):
            print("Let's start to questions. You will be asked to enter the option you choose (a/b/c/d).\n \
Then your score will be calculated based on your answers and the difficlty of the questions.\n \
Question {}: {}\nOptions are:\n{}\n{}\n{}\n{}\n".format(i+1,questions[i]['text'],
            questions[i]['options'][0],questions[i]['options'][1],questions[i]['options'][2],questions[i]['options'][3]))
            answ=input("Your answer: ")
            if questions[i]['difficulty']=='easy':
                score+=5
                if answ==questions[i]['answer']:
                    your_score+=5
            elif questions[i]['difficulty']=='difficult':
                score+=10
                if answ==questions[i]['answer']:
                    your_score+=10
            print('Your score is {} out of {}'.format(your_score,score))