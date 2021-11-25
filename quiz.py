from question import Quiz
import json
import os


class BadInputException(Exception):
    def __init__(self, message='Input is not valid.'):
        self.message = message
        super().__init__(self.message)


class main:
    def __init__(self) -> None:
        print("Welcome to the quiz!\nDo you want to create or play a quiz?")
        self.choice = input("Enter create/play: ")
        if self.choice == 'create':
            return self.create_quiz()
        elif self.choice == 'play':
            return self.play_quiz()
        else:
            raise BadInputException()

    def create_quiz(self):
        quiz_name = input("Enter the name of the quiz : ")
        question_num = int(input("How many question ? : "))
        print(f"Thank you, let's enter the {question_num} question(s).")
        new_quiz = Quiz(quiz_name)
        for i in range(question_num):
            new_quiz.addQuestion(i+1)
        new_quiz.save()
        print("Quiz ready!")

    def play_quiz(self):
        self.quiz_names()
        if self.number_of_files == 0:
            print('Sorry there is no quiz available. Please create a quiz!')
        else:
            print(
                "Okay, let's get started\nEnter the name of the quiz you want to play. Options are: ")
            print(*self.names_of_files, sep='\n')
            self.kies = input("Your quiz: ")
            if not os.path.isfile('quizzes/'+self.kies+'.json'):
                raise BadInputException("Wrong name of quiz!")
            else:
                self.json_to_quiz(self.kies)

    def json_to_quiz(self, name):
        with open('quizzes/'+self.kies+'.json', 'r') as file:
            read = json.load(file)
            Quiz.play(read)

    def quiz_names(self):
        os.chdir("quizzes")
        # self.number_of_files = len(
        #     [name for name in os.listdir('.') if os.path.isfile(name)])
        # self.names_of_files = [name.split(
        #     ".")[0] for name in os.listdir('.') if os.path.isfile(name)]
        os.chdir("..")


if __name__ == "__main__":
    while True:
        main()
        choice1 = input(
            "clicking a for creating quiz or playing quiz otherwise the program will be terminated: ")
        if choice1 == 'a':
            main()
        else:
            break
