# Things to do
# - allow user to enter name
# - store name and score into a file
# - end game state
# - add other categories

import csv
import random
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

class Questions():
    """
    Represents an object that contains a list of questions and answers
    to ask the user
    contains points, representing how many points the user currently has
    contains lives, representing how many lives the user has remaining (starting with 3)
    contains a list of multiple choice questions and answers
    contains a list of true or false questions and answers
    """
    def __init__(self, points = 0, lives = 3, list_of_mc = [], list_of_tf = []):
        self.points = points
        self.lives = lives
        self.list_of_mc = self.addQuestionMc()
        self.list_of_tf = self.addQuestionTf()
    
    def __str__(self):
        str_mc = ""
        for m in self.list_of_mc:
            str_mc += str(m) + '\n'
        return "{}\n".format(str_mc)

    def addQuestionMc(self):
        """
        grabs the multiple choice questions and answers from a csv file
        and creates a new multiple choice question, adding them to the list of multiple
        choice questions
        Returns: a list of multiple choice questions
        """
        list = []
        with open('multiple_choice.csv', encoding='utf-8') as myFile:
            reader = csv.reader(myFile)
            for arr in reader:
                choices = {}
                title = arr[0]
                question = arr[1]
                answer = arr[2]
                choices[arr[3]] = arr[4]
                choices[arr[5]] = arr[6]
                choices[arr[7]] = arr[8]
                list.append(MultipleChoice(title, question, answer, choices))
            return list
        
    def addQuestionTf(self):
        """
        grabs the true or false questions and answers from a csv file
        and creates a new true or false question, adding them to the list of 
        the true or false questions
        Returns: a list of true or false questions
        """
        list = []
        with open('true_or_false.csv', encoding='utf-8') as myFile:
                reader = csv.reader(myFile)
                for arr in reader:
                    title = arr[0]
                    question = arr[1]
                    answer = arr[2]
                    list.append(TrueOrFalse(title, question, answer))
                return list
        
    def getRandQuest(self, cat):
        """
        takes in a type of question and grabs a random question
        from the list of questions based on the given type of question
        returns: a question
        """
        if cat == 'a':
            num = random.randint(0, len(self.list_of_mc)-1)
            q = self.list_of_mc[num]
            self.list_of_mc.pop(num)
            return q
        elif cat == 'b':
            num = random.randint(0, len(self.list_of_tf)-1)
            q = self.list_of_tf[num]
            self.list_of_tf.pop(num)
            return q

    def users_answer(self, cat):
        """
        takes in a selected type of question and gets the answer to the chosen
        question from the user, comparing their answer to the actual answer
        displays the question, number of points of the user, or lives left
        returns: whether the user was correct or incorrect
        """
        question = self.getRandQuest(cat)
        ROOT = tk.Tk()
        ROOT.withdraw()
        answer = simpledialog.askstring(title="Question",
                                  prompt=question)
        if question.compareAnswer(answer):
            if cat == 'a':
                self.points += 10
            elif cat == 'b':
                self.points += 5
            messagebox.showinfo("Information", 'Correct \nPoints count: ' + str(self.points))
            return 'Correct'
        else:
            self.lives -= 1
            messagebox.showinfo("Information", 'Incorrect \nLives left: ' + str(self.lives))
            return 'Incorrect'

class Question():
    """
    represents a generic question with a title, question, and answer
    """
    def __init__(self, title = '', question = '', answer = ''):
        self.title = title
        self.question = question
        self.answer = answer

    def __str__(self):
        return "Movie: {} \nQuestion: {} \n".format(self.title, self.question) 

    def compareAnswer(self, answer):
        """
        compares the given answer to the answer of this question
        return: boolean
        """
        return self.answer.lower() == answer.lower()

class MultipleChoice(Question):
    """
    represents a multiple choice question with a title, question, answer,
    and the choices of the question
    """
    def __init__(self, title = '', question = '', answer = '', choices = {}):
        self.choices = choices
        super().__init__(title, question, answer)

    def __str__(self):
        s = super().__str__()
        answer_list = []
        for k in self.choices:
            answer_list.append(str(k) + ': ' + str(self.choices[k]) + '\n')
        return s +  "\n{}".format(''.join(answer_list)) 
    
class TrueOrFalse(Question):
    """
    represents a true or false question with a title, question, and answer
    """
    def __init__(self, title = '', question = '', answer = False):
        super().__init__(title, question, answer)

    def __str__(self):
        return super().__str__()

def ask_questions():
    """
    asks the user questions, looking for input from the user on which type of question
    to choose, checks to see if the user has reached 0 lives or has reached 50 points
    """
    q = Questions()
    ROOT = tk.Tk()
    ROOT.withdraw()
    name = simpledialog.askstring(title="User",
                                  prompt="Enter your name:")
    while q.points < 50:
        cat = simpledialog.askstring(title="Trivia Game",
                                  prompt="Choose a type of question \n a. Multiple Choice \n b. True or False \n")
        question = q.users_answer(cat)
        if q.lives == 0:
            messagebox.showinfo("Information", 'You lose')
            break
    if q.points >= 50:
        messagebox.showinfo("Information", 'You win!')
    with open("leaderboard.txt", 'a') as myFile:
        myFile.write(str(name) + ": " + str(q.points) + "\n")

print(ask_questions())

# Questions to ask
# - leaderboard: the file is local to my computer, is that fine?
# - should I add the short answer questions?