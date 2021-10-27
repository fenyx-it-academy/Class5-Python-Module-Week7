import json
import os


class Quiz:
    """
    This class contains all quizes.
    """

    def __init__(self, name):
        self.name = name  # quiz name
        # every quiz has own questions . This list contains question class objects.
        self.questions = list()

    def addQuestion(self, id):
        """
        addquestion adding questions to that quiz.
        """
        text = input("Please enter the question : ")  # Question text
        while True:
            difficulty = input("Easy/Difficult : ")  # question difficulty
            if difficulty == "Easy" or difficulty == "Difficult" or difficulty == "easy" or difficulty == "difficult":
                break
            else:
                print("Please write 'easy' or 'difficult' ")
                # options
        optiona = input("a) : ")
        optionb = input("b) : ")
        optionc = input("c) : ")
        optiond = input("d) : ")
        correct_option = input("Correct option : ")
        options = {"a": optiona, "b": optionb, "c": optionc, "d": optiond}
        # all inputs are goes to Question class.
        question = Question(id, text, correct_option, difficulty, options)
        self.quizzes = question

        self.questions.append(question)

        def myFunc(e):
            """
            questions list sorted by id with the help of this function.
            """
            return e.id
        self.questions.sort(key=myFunc)

    def save_to_json(self):
        """
        all questions saved by quiz name in folder 'quizzes'
        """
        question_dict = dict()  # dict format contains all information about question before wrote the json format.
        for questionobject in self.questions:
            # questionobject takes object of Question class
            # paired by key-value in question_dict
            question_dict[questionobject.id] = {"text": questionobject.text,
                                                "answer": questionobject.answer,
                                                "difficulty": questionobject.difficulty,
                                                "options": questionobject.options}
        # in program path goes to the quizzes path
        cwd = os.path.join(os.getcwd(), "quizzes")
        os.chdir(cwd)

        with open(self.name+".json", "a") as jsonfile:
            # written in json format.
            json.dump(question_dict, jsonfile, indent=4, sort_keys=True)

    def play(self):
        # Let's play the quiz.
        self.totalpoint = 0

        for question in self.questions:
            # first objects are taken from question class
            print(
                f"Question {question.id} is : {question.text}\nOptions Are : ")
            for option, optiontext in list(question.options.items()):
                # for print inside of option dict.
                print(option+") "+optiontext)
            useranswer = input("Your Choice(a/b/c/d) : ")
            print(
                f"your answer is {useranswer}\nCorrect answer is {question.answer} ")
            if useranswer == question.answer:
                if question.difficulty == "easy" or question.difficulty == "Easy":
                    self.totalpoint += 5
                    print("Your score is 5 out 5")
                elif question.difficulty == "difficult" or question.difficulty == "Difficult":
                    self.totalpoint += 10
                    print("Your score is 10 out 10")
            elif useranswer != question.answer:
                if question.difficulty == "easy" or question.difficulty == "Easy":
                    print("Your score is 0 out 5")
                elif question.difficulty == "difficult" or question.difficulty == "Difficult":
                    print("Your score is 0 out 10")
        print(f"Your total score is {self.totalpoint}")


class Question:
    def __init__(self, id, text, answer, difficulty, options):
        self.id = id
        self.text = text
        self.answer = answer
        self.difficulty = difficulty
        self.options = options
