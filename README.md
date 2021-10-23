# Class5-Python-Module-Week7

## 1. Quiz

**General Info**
- You will create a quiz program. Users will be able to create quizzes or play existing quizzes.
- All information about each created quiz will be stored in `JSON` format under `quizzes` directory. Every quiz will have a name. For example; if the quiz name is `test`, it will be stored in `quizzes/test.json` file.

In this project you will have 2 files:

- question.py
- quiz.py

**question.py**

- You will have class `Question` with attributes: `id`, `text`, `answer`, `difficulty` and `options`.
- You will have class `Quiz` with attributes: `name` and `questions`. 
- Add `__init__` method to `Quiz` such as it will take `name` as parameter and also will initialize an empty `questions` array.
- The `Quiz` class will have following methods:
    - `addQuestion(id)` asks user 
        - the text of the question
        - the difficulty level of the question which can be `easy` or `difficult`. Keep asking until the user enters a valid input (easy or difficult)
        - the options for the question answer `a), b), c), d)`
        - the correct answer (a, b, c or d)
        - then creates a `Question` object with tha data you obtained from user. Lastly, adds this `Question` to `quizzes` attribute of `Quiz`.

    ```
    Thank you, let's enter 1 question(s).
    1) Please enter the question: What is ... ?
    What is the difficulty of the question? (easy/difficult) easy
    Please enter the options:
    a) option 1
    b) option 2
    c) option 3
    d) option 4
    What is the correct answer? (a/b/c/d) a
    ```
    - `save` method converts `Quiz` instance to json object and saves it into `quizzes/quizname.json`. quizname is equal to name field of `Quiz` object.
    - `play` method asks user the questions in the quiz. If the user answers it correctly, he gets points. If the question is easy, it is 5 points; if it is difficult, it is 10 points.
        - This method calculates 2 scores. First one is the score of the user and the second one is the total points can be obtained in the quiz. 
        - Lastly, print the user score out of total score.
    ```
    Let's start to questions. You will be asked to enter the option you choose (a/b/c/d).
    Then your score will be calculated based on your answers and the difficlty of the questions.

    Question 1 is: q1
    Options are:
    a) opt1
    b) opt2
    c) opt3
    d) opt4
    Your answer: b
    Your score is 0 out of 5
    ```

**quiz.py**
- This is the main file you will run to play the quiz.
- Define a custom exception called `BadInputException`.
- Add `if __name__ == '__main__'` statement and do following:
    - Ask user to choose one of `create` or `play` options. 
    ```
    Welcome to the quiz!

    Do you want to create or play a quiz? (Enter create/play)
    ```
    - If user chooses `create`, call `create_quiz()` method.
     - If user chooses `play`, call `play_quiz()` method.
    - If user chooses something else, raise `BadInputException` with message.
- There will be 4 different functions in this file. Their details are as follows:
    - `create_quiz()`: 
        - Asks user the name of the quiz and the number of the question he wants to ask. 
        - Then creates a `Quiz` object using the class object we have created and passes the name obtained from the user to this object. 
        - Then adds as many as question user asked for by calling `addQuestion` method of `Quiz`. Also passes `id` to the questions. E.g. the id of first question in the quiz will be 1.
        - Lastly, calls `save()` method of `Quiz` to save the quiz to a json file and prints "Quiz is ready!"
    - `quiz_names` returns the name of all files under `quizzes` directory.
    - `play_quiz()`:
        - Calls `quiz_names` functions to get existing quiz names.
        - If there is no quiz available prints "Sorry there is no quiz available. Please create a quiz!"
        - If there are quizzes displays the name of all existing quizzes and asks the user the name of the quiz he wants to play.
        ```
        Okay, let's get started
        Enter the name of the quiz you want to play. Options are:
         -  other_test
         -  test
        Your quiz:
        ```
        - If the user enters an invalid quiz name, raise `BadInputException`
        - If the user enters a valid quiz name, calls `json_to_quiz(name)` function with quiz name to convert the input of JSON file to a`Quiz` object.
        - Lastly calls `play()` method for `Quiz` object.
    - `quiz_names` return the list of all file names under `quizzes` directory.
    - `json_to_quiz(name)` reads the given input file and converts the JSON data inside the file to `Quiz`. For example; if the given name parameter is `test`, the method reads the content of `quizzes/test.json` file. Using this content, the function creates and returns a `Quiz` object.

## 2. India

Write a method in Python to read lines from a text file `india.txt`, to find and display the occurrence of the word 'India'. For example, if the content of the file is:

```
India is the fastest-growing economy. India is 
looking for more investments around the globe. The 
whole world is looking at India as a great market. 
Most of the Indians can foresee the heights that 
India is capable of reaching.
```
The output should be 4.

## 3. To Json

1. Create a `Product` class with attribute `name`, `brand` and `price`.
2. Add `toJson` method to `Product` class. The method should convert class object to JSON.
3. Create a `Brand` class with attirbute `name` and `year`.
4. Create a `Product` object and use `Brand` object for `brand` field.
4. Call `toJson` method.


## Hackerrank Questions

1. Utopian Tree: https://www.hackerrank.com/challenges/utopian-tree/problem

2. Picking Numbers: https://www.hackerrank.com/challenges/picking-numbers/problem

3. Validating and Parsing Email Addresses: https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

4. Mini-Max Sum: https://www.hackerrank.com/challenges/mini-max-sum/problem
