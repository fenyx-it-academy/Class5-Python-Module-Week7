import question
import os
import json


class BadInputException(Exception):
    pass


def create_quiz(quizname, number_of_questions):
    # according to user , created Quiz class.
    quizname = question.Quiz(quizname)
    for id in range(1, number_of_questions+1):
        # according to user , Questions are added in the Quiz.
        quizname.addQuestion(id)
    quizname.save_to_json()  # saved in json
    print("Quiz is Ready")


def json_to_quiz(name):
    # from json file are creating Questions objects .
    with open(name) as json_file:
        data = json.load(json_file)  # dict type of Questions.
    name = question.Quiz(name)
    for id in data:
        # all past inputs are taking from json for Question object.
        answer = data[id]["answer"]
        difficulty = data[id]["difficulty"]
        options = data[id]["options"]
        text = data[id]["text"]
        name.quizzes = question.Question(id, text, answer, difficulty, options)
        # added question list of Quiz's object.
        name.questions.append(name.quizzes)
    return name


def quiz_names():
    for i, j, k in os.walk(os.path.join(os.getcwd(), "quizzes")):
        return k


def play_quiz():
    quiznames = quiz_names()
    for names in quiznames:
        print("Quizname : ", names)
    os.chdir(os.path.join(os.getcwd(), "quizzes"))
    if len(quiznames) == 0:
        print("Sorry there is no quiz available. Please create a quiz!")
    else:
        quiz = input("which quiz do you want play ? (with filetype) : ")
        if quiz not in quiznames:
            raise BadInputException
        else:
            # jsontoquiz returned Quiz object which can use Quiz class's methot
            json_to_quiz(quiz).play()


if __name__ == "__main__":
    chooice = input("Create or Play ? : ")
    print("Welcome to the quiz!".center(50, "*"))
    if chooice == "create":
        quizname = input("What will be your quiz name : ")
        noq = int(input("How Many question will it contain ? :"))
        create_quiz(quizname, noq)
    elif chooice == "play":
        play_quiz()
    else:
        raise BadInputException
