"""
Author: Brenden Johnson
Assignment: Lab 9
Due Date: 4-22-2023
Course: 2520.01
"""
import random


class Student:
    name = None
    id = 0
    current_score = 0
    highest_score = 0

    def __init__(self, name, id, current_score = 0, highest_score = 0):
        self.name = name
        self.id = id
        self.current_score = current_score
        self.highest_score = highest_score

    def setScore(self, score):
        self.current_score = score
        if score > self.highest_score:
            self.highest_score = score


class Question:
    quest = None
    a = None
    b = None
    c = None
    d = None
    correct = None

    def __init__(self, ques, qa, qb, qc, qd, ans):
        self.quest = ques
        self.a = qa
        self.b = qb
        self.c = qc
        self.d = qd
        self.correct = ans


class Test:
    questions = []
    scores = []


    def __init__(self, questionList):
        self.questions = questionList

    def begin(self, student):
        score = 0
        quizquestions = [self.questions[i] for i in random.sample(range(0, 12), 5)]
        for question in quizquestions:
            print(question.quest)
            print("A. ", question.a)
            print("B. ", question.b)
            print("C. ", question.c)
            print("D. ", question.d)
            answer = input("Enter answer(A, B, C, D): ")
            if answer == question.correct:
                score += 1
        else:
            print("Your score is: ", score)
            student.setScore(score)
            self.scores.append(score)


def initializeQuestions():
    questionList = []
    questionList.append(Question(
        "Where is Cal Poly Pomona located?",
        "Texas",
        "California",
        "Nevada",
        "Washington",
        "B")
    )
    questionList.append(Question(
        "On your student records system, what does CSU stand for",
        "California State Universities",
        "Colorado State Universities",
        "Color Sparkling Unicorn",
        "Canadian Swan Upping",
        "A")
    )
    questionList.append(Question(
        "How many Infinity Stones are there?",
        "3",
        "5",
        "6",
        "10",
        "C")
    )
    questionList.append(Question(
        "What is the only food that cannot go bad?",
        "Dark chocolate",
        "Peanut butter",
        "Canned tuna",
        "Honey",
        "D")
    )
    questionList.append(Question(
        "Which was René Magritte’s first surrealist painting? ",
        "Not to Be Reproduced",
        "Personal Values",
        "The Lovers",
        "The Lost Jockey",
        "D")
    )
    questionList.append(Question(
        "What 90s boy band member bought Myspace in 2011?",
        "Nick Lachey",
        "Justin Timberlake",
        "Shawn Stockman",
        "AJ McLean",
        "B")
    )
    questionList.append(Question(
        "What is the most visited tourist attraction in the world?",
        "Statue of Liberty",
        "Eiffel Tower",
        "Great Wall of China",
        "Colosseum",
        "B")
    )
    questionList.append(Question(
        "What’s the name of Hagrid’s pet spider?",
        "Nigini",
        "Crookshanks",
        "Aragog",
        "Mosag",
        "C")
    )
    questionList.append(Question(
        "What’s the heaviest organ in the human body?",
        "Brain",
        "Liver",
        "Skin",
        "Heart",
        "B")
    )
    questionList.append(Question(
        "Who made the third most 3-pointers in the Playoffs in NBA history?",
        "Kevin Durant",
        "JJ Reddick",
        "Lebron James",
        "Kyle Korver",
        "C")
    )
    questionList.append(Question(
        "Which US city is the sunniest major city and sees more than 320 sunny days each year?",
        "Phoenix – Phoenix sees more than 320 sunny days each year.",
        "Miami",
        "San Francisco",
        "Austin",
        "A"
    ))
    questionList.append(Question(
        "What is the oldest soft drink in the United States?",
        "Coca Cola",
        "Pepsi",
        "Dr. Pepper",
        "Canada Dry Ginger Ale",
        "C")
    )
    questionList.append(Question(
        "What river passes through New Orleans, Louisiana?",
        "Orleans River",
        "Mississippi River",
        "Atchafalaya River",
        "Colorado River",
        "B")
    )
    return questionList



def main():
    print("Welcome to the test taking system")
    test1 = Test(initializeQuestions())
    while True:
        print("Press: 1 To take test, 2 to view test statics 3 to terminate")
        option = int(input("-"))
        if option == 1:
            name = input("Provide name to take test: ")
            s1 = Student(name, 1)
            test1.begin(s1)
        elif option == 2:
            scores = test1.scores
            print(len(scores), " students have taken the test")
            sm, avg = 0, 0
            for score in scores:
                sm += score
            else:
                if len(scores) != 0:
                    avg = sm / len(scores)
            print("The average score is", avg)
        else:
            break


main()

'''
Output

Welcome to the test taking system
Press: 1 To take test, 2 to view test statics 3 to terminate
-1
Provide name to take test: bob
What is the only food that cannot go bad?
A.  Dark chocolate
B.  Peanut butter
C.  Canned tuna
D.  Honey
Enter answer(A, B, C, D): A
How many Infinity Stones are there?
A.  3
B.  5
C.  6
D.  10
Enter answer(A, B, C, D): C
Which US city is the sunniest major city and sees more than 320 sunny days each year?
A.  Phoenix – Phoenix sees more than 320 sunny days each year.
B.  Miami
C.  San Francisco
D.  Austin
Enter answer(A, B, C, D): A
Where is Cal Poly Pomona located?
A.  Texas
B.  California
C.  Nevada
D.  Washington
Enter answer(A, B, C, D): B
What’s the name of Hagrid’s pet spider?
A.  Nigini
B.  Crookshanks
C.  Aragog
D.  Mosag
Enter answer(A, B, C, D): C
Your score is:  4
Press: 1 To take test, 2 to view test statics 3 to terminate
-2
1  students have taken the test
The average score is 4.0
Press: 1 To take test, 2 to view test statics 3 to terminate
-1
Provide name to take test: randy
Which US city is the sunniest major city and sees more than 320 sunny days each year?
A.  Phoenix – Phoenix sees more than 320 sunny days each year.
B.  Miami
C.  San Francisco
D.  Austin
Enter answer(A, B, C, D): A
How many Infinity Stones are there?
A.  3
B.  5
C.  6
D.  10
Enter answer(A, B, C, D): C
Who made the third most 3-pointers in the Playoffs in NBA history?
A.  Kevin Durant
B.  JJ Reddick
C.  Lebron James
D.  Kyle Korver
Enter answer(A, B, C, D): C
Which was René Magritte’s first surrealist painting? 
A.  Not to Be Reproduced
B.  Personal Values
C.  The Lovers
D.  The Lost Jockey
Enter answer(A, B, C, D): A
What’s the heaviest organ in the human body?
A.  Brain
B.  Liver
C.  Skin
D.  Heart
Enter answer(A, B, C, D): B
Your score is:  4
Press: 1 To take test, 2 to view test statics 3 to terminate
-2
2  students have taken the test
The average score is 4.0
Press: 1 To take test, 2 to view test statics 3 to terminate
-1
Provide name to take test: jessica
What is the only food that cannot go bad?
A.  Dark chocolate
B.  Peanut butter
C.  Canned tuna
D.  Honey
Enter answer(A, B, C, D): C
Where is Cal Poly Pomona located?
A.  Texas
B.  California
C.  Nevada
D.  Washington
Enter answer(A, B, C, D): C
What 90s boy band member bought Myspace in 2011?
A.  Nick Lachey
B.  Justin Timberlake
C.  Shawn Stockman
D.  AJ McLean
Enter answer(A, B, C, D): D
What is the most visited tourist attraction in the world?
A.  Statue of Liberty
B.  Eiffel Tower
C.  Great Wall of China
D.  Colosseum
Enter answer(A, B, C, D): D
Which was René Magritte’s first surrealist painting? 
A.  Not to Be Reproduced
B.  Personal Values
C.  The Lovers
D.  The Lost Jockey
Enter answer(A, B, C, D): C
Your score is:  0
Press: 1 To take test, 2 to view test statics 3 to terminate
-2
3  students have taken the test
The average score is 2.6666666666666665
Press: 1 To take test, 2 to view test statics 3 to terminate
-3
'''
