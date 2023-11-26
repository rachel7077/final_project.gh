# Things to Do
# - figure out where to use inheritance

import csv
import random
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

class Questions():
    def __init__(self, points = 0, lives = 3, list_of_mc = []):
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
            print('Lives left: ' + str(self.lives))
            messagebox.showinfo("Information", 'Incorrect \nLives left: ' + str(self.lives))
            return 'Incorrect'

class MultipleChoice():
    def __init__(self, title = '', question = '', answer = '', choices = {}):
        self.title = title
        self.question = question
        self.answer = answer
        self.choices = choices

    def __str__(self):
        answer_list = []
        for k in self.choices:
            answer_list.append(str(k) + ': ' + str(self.choices[k]) + '\n')
        return "Title: {} \nQuestion: {} \n{}".format(self.title, self.question, ''.join(answer_list)) 

    def compareAnswer(self, answer):
        return self.answer == answer
    
class TrueOrFalse():
    def __init__(self, title = '', question = '', answer = False):
        self.title = title
        self.question = question
        self.answer = answer

    def __str__(self):
        return "Title: {} \nQuestion: {} \n".format(self.title, self.question) 

    def compareAnswer(self, answer):
        return self.answer.lower() == answer.lower()

q = Questions()
ROOT = tk.Tk()
ROOT.withdraw()
while q.points < 50:
    cat = simpledialog.askstring(title="Test",
                                  prompt="Choose a type of question \n a. Multiple Choice \n b. True or False \n")
    question = q.users_answer(cat)
    if q.lives == 0:
        messagebox.showinfo("Information", 'You lose')
        break
if q.points >= 50:
    messagebox.showinfo("Information", 'You win!')