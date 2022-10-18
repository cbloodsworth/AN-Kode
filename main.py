from tkinter import *
from tkinter import ttk
from turtle import bgcolor
import webbrowser
import json

PROBLEM_BASE = [1,121,125,226,242,704,733,235,110,141,232,20,21,278,383,70,409,206,169,67,543,876,104,217,53,133,150,207,208,322,238,155,98,200,994,57,542,973,3,15,102,33,39,46,56,236,981,721,75,11,17,79,438,310,621,146,230,76,297,42,295,127,224,1235,23,84]

class Problem:
    def __init__(self, name, number, link):
        self.name = name
        self.number = number
        self.link = link
    link = "null"
    name = "null"
    number = -1
    never_completed = True

def incrementProblemIndex():
    global problem_index
    problem_index += 1
    showProblem(problem_array[problem_index])



# Given a problem object, display the title, link and choices for perceived difficulty.
def showProblem(problem):
    def callback():
        webbrowser.open_new_tab(problem.link)

    ttk.Label(frm, text=problem.name).grid(column=0, row=0)
    ttk.Button(frm, text=problem.link, command=callback, cursor="hand2").grid(column=0, row=1)
    
    if problem.never_completed:
        showOptions("1010")
        never_completed = False
    else:
        showOptions("1111")


def showOptions(options_bin):
    for i, n in enumerate(options_bin):
        if n == "1":
            showButton(i)

def displayButton(name, col=0):
    ttk.Button(frm, text=name, command=incrementProblemIndex).grid(column=col, row = 2)

    
# again=0,hard=1,good=2,easy=3
def showButton(button):
    match button:
        case 0:
            displayButton("Again", 1)
        case 1:
            displayButton("Hard", 2)
        case 2:
            displayButton("Good", 3)
        case 3:
            displayButton("Easy", 4)

def main():
    with open('problems.json', 'r') as json_file:
        json_load = json.load(json_file)

    global problem_array
    problem_array = []
    
    for i in range(1788):
        if json_load['stat_status_pairs'][i]["stat"]["question_id"] in PROBLEM_BASE:
            name = json_load['stat_status_pairs'][i]["stat"]["question__title"]
            number = json_load['stat_status_pairs'][i]["stat"]["question_id"]
            link = "https://leetcode.com/problems/" + json_load['stat_status_pairs'][i]["stat"]["question__title_slug"]
            problem_array.append(Problem(name,number,link))
    
    root.title("AN-Kode")
    root.geometry("512x512")
    frm.grid()
    global problem_index 
    problem_index = 0
    showProblem(problem_array[problem_index])
    root.mainloop()

root = Tk()
frm = ttk.Frame(root, padding=10)
main()