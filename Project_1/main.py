# Project Summary:
# A simple calculator 
from tkinter import *

# Expression is what we are trying to calculate, declared globally
expression = "" 

# Every time a number is pressed, it is added onto the expression 
def press(num):
    global expression
    expression = expression + str(num)

    equation.set(expression) # ???? Not sure what this line does


# This function will evaluate 
def equalPress():
    # Try and Catch Statement
    # Cases:
    # Divide by 0
    try:

        global expression
        total = str(eval(expression)) # calling the eval function 
        equation.set(total)

    except:

        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":

    # creating the gui window
    gui = Tk()

    # Setting the title
    gui.title("Simple Calculator")

    # Setting the background color of the window
    gui.configure(background="light green")

    # Setting the length and width of the calculator
    gui.geometry("300x300")

    # gui.
    
    pass