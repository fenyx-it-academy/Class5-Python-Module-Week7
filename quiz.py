from question import Quiz
import os
import json
class BadInputException(Exception):
    def __init__(self,message='Invalid input'):
        super().__init__(self.message)
        self.message = message

class main:
    def __init__(self) -> None:
        print('Welcome to quiz.\nDo you want to play or create a quiz?')
        option = input('create or play:')
        if option == 'create':
            return self.create_quiz()
        elif option == 'play':
            return self.play_quiz()
        else:
            raise BadInputException()
    
    def create_quiz(self):
        quiz_name=input('Enter the quiz name')
        amount_of_questions=input('Enter the question amount:')
        print('The quiz will have {} question'.format(amount_of_questions))
        new_quizz=Quiz(quiz_name)
        for i in range(int(amount_of_questions)):
            new_quizz.addQuestion(i+1)
        new_quizz.save()
        print('Quiz is saved')
    def play_quiz(self):
        self.quiz_names()
        if self.number_of_files==0:
            print('Sorry there is no quiz available. Please create a quiz!')
        else:
            print("Okay, let's get started\nEnter the name of the quiz you want to play. Options are: ")
            print(*self.names_of_files,sep='\n')
            choice=input("Your quiz: ")
            if choice not in self.names_of_files:
                raise BadInputException("Wrong name of quiz!")
            else:
                self.json_to_quiz(choice)

    def quiz_names(self):
        os.chdir("quizzes")
        self.number_of_files=len([name for name in os.listdir('.') if os.path.isfile(name)])
        self.names_of_files=[name.split(".")[0]  for name in os.listdir('.') if os.path.isfile(name)]
        os.chdir("..")


    def json_to_quiz(self,name):
        with open("quizzes/{}.json".format(name),'r') as file:
            read=json.load(file)
            Quiz.play(read)
if __name__ == "__main__":
    while True:
        main()
        choice=input("clicking a for creating quiz or playing quiz otherwise the program will be terminated: ")
        if choice=='a':
            main()
        else:
            break
