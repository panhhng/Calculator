from tkinter import *

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 310

calculation = ""

def addItem(item):
    global calculation
    calculation += str(item)
    
    result.delete(1.0, "end")
    result.insert(1.0, calculation)
    
def operate():
    global calculation
    calculation = str(eval(calculation))
    
    try:
        result.delete(1.0, "end")
        result.insert(1.0, calculation)
    except:
        clear()
        result.insert(1.0, "Syntax error")
    
def clear():
    global calculation
    calculation = ""
    
    result.delete(1.0, "end")
    
def percent():
    global calculation
    calculation = str(eval(calculation) / 100)

    result.delete(1.0, "end")
    result.insert(1.0, calculation)
    
def sign():
    global calculation
    calculation = str(eval("-" + calculation))

    result.delete(1.0, "end")
    result.insert(1.0, calculation)
    
window = Tk()
window.title("Calculator")

window.resizable(False, False)
window.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

result = Text(window, height=2, width=46, font=("Arial, 24"))
result.grid(columnspan=12)

btn = Button(window, text="AC", command=lambda: clear(), width=8, font=("Arial, 24"))
btn.grid(row=2, column=1)
btn = Button(window, text="+/-", command=sign, width=8, font=("Arial, 24"))
btn.grid(row=2, column=2)
btn = Button(window, text="%", command=lambda: percent(), width=8, font=("Arial, 24"))
btn.grid(row=2, column=3)
btn = Button(window, text="/", command=lambda: addItem("/"), width=8, font=("Arial, 24"))
btn.grid(row=2, column=4)

btn = Button(window, text="7", command=lambda: addItem(7), width=8, font=("Arial, 24"))
btn.grid(row=3, column=1)
btn = Button(window, text="8", command=lambda: addItem(8), width=8, font=("Arial, 24"))
btn.grid(row=3, column=2)
btn = Button(window, text="9", command=lambda: addItem(9), width=8, font=("Arial, 24"))
btn.grid(row=3, column=3)
btn = Button(window, text="*", command=lambda: addItem("*"), width=8, font=("Arial, 24"))
btn.grid(row=3, column=4)

btn = Button(window, text="4", command=lambda: addItem(4), width=8, font=("Arial, 24"))
btn.grid(row=4, column=1)
btn = Button(window, text="5", command=lambda: addItem(5), width=8, font=("Arial, 24"))
btn.grid(row=4, column=2)
btn = Button(window, text="6", command=lambda: addItem(6), width=8, font=("Arial, 24"))
btn.grid(row=4, column=3)
btn = Button(window, text="-", command=lambda: addItem("-"), width=8, font=("Arial, 24"))
btn.grid(row=4, column=4)

btn = Button(window, text="1", command=lambda: addItem(1), width=8, font=("Arial, 24"))
btn.grid(row=5, column=1)
btn = Button(window, text="2", command=lambda: addItem(2), width=8, font=("Arial, 24"))
btn.grid(row=5, column=2)
btn = Button(window, text="3", command=lambda: addItem(3), width=8, font=("Arial, 24"))
btn.grid(row=5, column=3)
btn = Button(window, text="+", command=lambda: addItem("+"), width=8, font=("Arial, 24"))
btn.grid(row=5, column=4)

btn = Button(window, text="0", command=lambda: addItem("0"), width=19, font=("Arial, 24"))
btn.grid(row=6, column=1, columnspan=2)
btn = Button(window, text=",", command=lambda: addItem("."), width=8, font=("Arial, 24"))
btn.grid(row=6, column=3)
btn = Button(window, text="=", command=operate, width=8, font=("Arial, 24"))
btn.grid(row=6, column=4)

btn = Button(window, text="(", command=lambda: addItem("("), width=19, font=("Arial, 24"))
btn.grid(row=7, column=1, columnspan=2)
btn = Button(window, text=")", command=lambda: addItem(")"), width=19, font=("Arial, 24"))
btn.grid(row=7, column=3, columnspan=2)

window.mainloop()