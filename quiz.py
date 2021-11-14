from question import Quiz
import os
import json

class BadInputException(Exception):
    def __init__(self,message = "You shouşd entry 'create' or 'play'!!! "):
        self.message = message
        super().__init__(self.message)
    if __name__ == '__main__':
        def __init__(self):
            print("Welcome to the quiz!")
            self.choice = input("Do you want to create or play a quiz? (Enter create/play)")
            if self.choice == "create":
                return self.create_quiz()
            elif self.choice == "play":
                return self.play_quiz()
            else:
                raise BadInputException(Exception)
        
        def create_quiz():
            quiz_name = input("What's quiz name?: ")
            num = input("Which number of the question do you want to ask?: ")
            quiz = Quiz(quiz_name)
            for i in range(num):
                quiz.addQuestion(i+1)
            quiz.save()
            print("Quiz ready!")
        def play_quiz(self):
            self.quiz_name
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
        def json_to_quiz(self,name):
            with open("quizzes/{}.json".format(name),'r') as file:
                read=json.load(file)
                Quiz.play(read)
        def quiz_names(self):
            os.chdir("quizzes")
            self.number_of_files=len([name for name in os.listdir('.') if os.path.isfile(name)])
            self.names_of_files=[name.split(".")[0]  for name in os.listdir('.') if os.path.isfile(name)]
            os.chdir("..")
if __name__ == "__main__":
    while True:
        main()
        choice=input("clicking a for creating quiz or playing quiz otherwise the program will be terminated: ")
        if choice=='a':
            main()
        else:
            break            
