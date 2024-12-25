import tkinter
from tkinter import *

# Initialize the main window
root = Tk()
root.title('Calculator')
root.geometry('570x600+100+200')
root.resizable(False, False)
root.configure(bg='#17161b')

# Global variable to store the equation
equation = ""

# Function to show input in the label
def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

# Function to clear the input
def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

# Function to evaluate the equation
def calculate():
    global equation
    try:
        # Evaluate the equation and update the label
        result = eval(equation)
        label_result.config(text=str(result))
        equation = str(result)  # Update the equation to allow further calculations
    except:
        label_result.config(text='error')
        equation = ""  # Reset the equation in case of error

# Label to display the result or equation
label_result = Label(root, width=25, height=2, text="", font=('arial', 30))
label_result.pack()

# Buttons for the calculator
Button(root, text='C', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#3697f5', command=clear).place(x=10, y=100)
Button(root, text='()', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('()')).place(x=150, y=100)
Button(root, text='%', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('%')).place(x=290, y=100)
Button(root, text='/', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('/')).place(x=430, y=100)

Button(root, text='7', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('7')).place(x=10, y=200)
Button(root, text='8', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('8')).place(x=150, y=200)
Button(root, text='9', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('9')).place(x=290, y=200)
Button(root, text='*', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('*')).place(x=430, y=200)

Button(root, text='4', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('4')).place(x=10, y=300)
Button(root, text='5', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('5')).place(x=150, y=300)
Button(root, text='6', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('6')).place(x=290, y=300)
Button(root, text='-', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('-')).place(x=430, y=300)

Button(root, text='1', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('1')).place(x=10, y=400)
Button(root, text='2', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('2')).place(x=150, y=400)
Button(root, text='3', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('3')).place(x=290, y=400)
Button(root, text='+', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('+')).place(x=430, y=400)

Button(root, text='0', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('0')).place(x=10, y=500)
Button(root, text='00', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('00')).place(x=150, y=500)
Button(root, text='.', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#2a2d36', command=lambda: show('.')).place(x=290, y=500)
Button(root, text='=', width=5, height=1, font=('arial', 30, 'bold'), bd=1, fg='#fff', bg='#fe9037', command=calculate).place(x=430, y=500)


root.mainloop()
