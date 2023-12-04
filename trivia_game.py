# Things to do
# - add other categories
# - ask about editing window for trivia game

import csv
import random
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

class Question():
    """
    represents a generic question with a movie title, question, and answer
    """
    def __init__(self, title = '', question = '', answer = ''):
        self.title = title
        self.question = question
        self.answer = answer

    def __str__(self):
        return "Movie: {} \nQuestion: {} \n".format(self.title, self.question) 

    def compare_answer(self, answer):
        """
        compares the given answer to the answer of this question
        return: boolean
        """
        return self.answer.lower() == answer.lower()

class MultipleChoice(Question):
    """
    represents a multiple choice question with a movie title, question, answer,
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

class Quiz():
    """
    Represents an object that contains a list of questions and answers
    to ask the user
    contains points, representing how many points the user currently has
    contains lives, representing how many lives the user has remaining (starting with 3)
    contains a list of questions that can either be multiple choice or short answer
    """
    def __init__(self, points = 0, lives = 3, list_of_q = []):
        self.points = points
        self.lives = lives
        self.list_of_q = list_of_q
    
    def __str__(self):
        str_q = ""
        for m in self.list_of_q:
            str_q += str(m) + '\n'
        return "{}\n".format(str_q)
        
    def add_question(self, questions):
        """
        allows the user to add questions to the quiz
        """
        for q in questions:
            self.list_of_q.append(q)
        
    def get_rand_quest(self, cat):
        """
        takes in a type of question and grabs a random question
        from the list of questions based on the given type of question
        if an incorrect category was given, prompts the user to try again
        returns: a question
        """
        list_of_mc = []
        list_of_tf = []
        # adding multiple choice questions to a list of multiple choice questions
        for q_mc in self.list_of_q:
            if isinstance(q_mc, MultipleChoice):
                list_of_mc.append(q_mc)
        # adding true or false questions to a list of true or false questions
        for q_tf in self.list_of_q:
            if isinstance(q_tf, TrueOrFalse):
                list_of_tf.append(q_tf)
        # returns a random multiple choice question
        if cat == 'a':
            num = random.randint(0, len(list_of_mc)-1)
            q = list_of_mc[num]
            list_of_mc.pop(num)
            return q
        # returns a random true or false question
        elif cat == 'b':
            num = random.randint(0, len(list_of_tf)-1)
            q = list_of_tf[num]
            list_of_tf.pop(num)
            return q
        else:
            return 'try again'

    def users_answer(self, cat):
        """
        takes in a selected type of question and gets the answer to the chosen
        question from the user, comparing their answer to the actual answer
        displays the question, number of points of the user, or lives left
        returns: whether the user was correct or incorrect
        """
        question = self.get_rand_quest(cat)
        ROOT = tk.Tk()
        ROOT.withdraw()
        # if the user enters an incorrect category, prompts the user to try again
        if question == 'try again':
            messagebox.showinfo("Information", 'Try again ')
        else:
            answer = simpledialog.askstring(title="Question",
                                  prompt=question)
            if question.compare_answer(answer):
                self.points += 10
                messagebox.showinfo("Information", 'Correct \nPoints count: ' + str(self.points))
                return 'Correct'
            else:
                self.lives -= 1
                messagebox.showinfo("Information", 'Incorrect \nLives left: ' + str(self.lives))
                return 'Incorrect'

def list_of_mc(file):
    """
    creates a list of multiple choice questions from the given file
    Return: a list of multiple choice questions
    """
    list_mc = []
    with open(file, encoding='utf-8') as myFile:
        reader = csv.reader(myFile)
        for arr in reader:
            choices = {}
            title = arr[0]
            question = arr[1]
            answer = arr[2]
            choices[arr[3]] = arr[4]
            choices[arr[5]] = arr[6]
            choices[arr[7]] = arr[8]
            list_mc.append(MultipleChoice(title, question, answer, choices))
    return list_mc

def list_of_tf(file):
    """
    creates a list of true or false questions from the given file
    Return: a list of true or false questions
    """
    list_tf = []
    with open(file, encoding='utf-8') as myFile:
        reader = csv.reader(myFile)
        for arr in reader:
            title = arr[0]
            question = arr[1]
            answer = arr[2]
            list_tf.append(TrueOrFalse(title, question, answer))
    return list_tf

def ask_questions():
    """
    asks the user questions, looking for input from the user on which type of question
    to choose, checks to see if the user has reached 0 lives or has reached 50 points
    """
    # creates lists of multiple choice and true or false questions
    list_mc = list_of_mc('multiple_choice.csv')
    list_tf = list_of_tf('true_or_false.csv')

    # adds the questions to a quiz
    q = Quiz()
    q.add_question(list_mc)
    q.add_question(list_tf)

    ROOT = tk.Tk()
    ROOT.withdraw() 
    name = simpledialog.askstring(title="User",
                                  prompt="Enter your name:")
    messagebox.showinfo("Information", 'How to Play\nType a or b for multiple choice or true or false. \
                        \n If choosing multiple choice, type the letter of the response in. \n If choosing true or false, \
                        type true or false in.')
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
        myFile.write("\n" + str(name) + ": " + str(q.points))
    leaderboard()
    close()
    
def close():
   """
   Exits out of tk.inter when game has been completed
   """
   end = tk.Tk()
   end.quit()

def leaderboard():
    """
    gets the top three scores from the leaderbord txt file
    Return: a messagebox containing the top three scores and scorers
    """
    dict = {}
    with open("leaderboard.txt", 'r') as readFile:
        while True:
            line = readFile.readline()
            if not line:
                break
            strings = "".join(line).strip("\n")
            list_user = strings.split(":")
            if len(list_user) >= 2:
                name = list_user[0]
                score = list_user[1]
                dict[name] = score
        sorted_dict = sorted(dict.items(), key=lambda x:x[1])
        dict_len = len(sorted_dict)
        top_score = sorted_dict[dict_len-1]
        second_score = sorted_dict[dict_len-2]
        third_score = sorted_dict[dict_len-3]
        if dict_len >= 3:
            messagebox.showinfo("Leaderboard", "Leaderboard \n1. " + top_score[0] + ": " + top_score[1] + " points" + "\n2. " + second_score[0] + ": " + second_score[1] + " points" + "\n3. " + third_score[0] + ": " + third_score[1] + " points")
        elif dict_len == 2:
            messagebox.showinfo("Leaderboard", "Leaderboard \n1. " + top_score[0] + ": " + top_score[1] + " points" + "\n2. " + second_score[0] + ": " + second_score[1] + " points")
        elif dict_len == 1:
            messagebox.showinfo("Leaderboard", "Leaderboard \n1. " + top_score[0] + ": " + top_score[1] + " points")
        else:
            messagebox.showinfo("Leaderboard", "No top scorers.")

#print(ask_questions())