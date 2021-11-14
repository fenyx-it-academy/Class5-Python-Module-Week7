import json
class Question:
    def __init__(self,id,text,answer,difficulty,options):
        self.id = id
        self.text =text
        self.answer =answer
        self.difficulty = difficulty
        self.options = options
    def __str__(self):
        return self.text,self.answer,self.difficulty,self.options

class Quiz:
    def __init__(self,name):
        self.name = name
        self.questions = []

    def addQuestion(self,id):
        self.id = id
        question_text = input("Please entry your question!: ")
        difficulty = input("Please choose level of questions.. Easy or difficult: ")
        options = [("a) "+input("a: ")),("b) "+input("b: ")),("c) "+input("c: ")),("d) "+input("d: "))]
        answer = input("Choose an answer from a,b,c or d: ")
        datas = Question(question_text,answer,difficulty,options)
        self.questions.append({"id": self.id,"question_text":datas.__str__()[0],"difficulty":datas.__str__()[1],
        "options":datas.__str__()[2],"answer":datas.__str__()[3]})

    def save(self):
        with open(f"quizzes/{self.name}.json","w") as f:
            json.dump(self.questions,f)

    def play(questions = []):
        score=0
        your_score=0
        for i in questions:
            print(f"You will be asked to enter the option you choose (a/b/c/d).\n \
Question {i['id']}: {i['text']}\nOptions are:\n{i['options'][0]}\n{i['options'][1]}\n{i['options'][2]}\n{i['options'][3]}\n")
            answ=input("Your answer: ")
            if i['difficulty']=='easy':
                score+=5
                if answ==i['answer']:
                    your_score+=5
            elif i['difficulty']=='difficult':
                score+=10
                if answ==i['answer']:
                    your_score+=10
            print('Your score is {} out of {}'.format(your_score,score))
