#Tkinter is the standard GUI library for Python
import tkinter as tk
import math

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")
      


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root=tk.Tk()
root.title("Calculator")  #for setting the title of screen
root.geometry("300x320")  #for setting the size of screen
#root.configure(bg='black')

#for the Text area calculation
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24), borderwidth=5)
text_result.grid(columnspan=5)

#for open parenthesis
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_open.grid(row=2, column=1)

#for percentage button
btn_percentage = tk.Button(root, text="%", command=lambda: add_to_calculation("/100"), width=5, font=("Arial", 14))
btn_percentage.grid(row=2, column=2)


#for the pi button
btn_pi = tk.Button(root, text="\u03C0", command=lambda: add_to_calculation("*(22/7)"), width=5, font=("Arial", 14))
btn_pi.grid(row=2, column=3)

#for the clear the all text from screen of calculator
btn_clear = tk.Button(root, text="C", command=clear_field, width=5, font=("Arial", 14), bg="red", fg="white")
btn_clear.grid(row=2, column=4)

#for the close parenthesis
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_close.grid(row=3, column=1)

#for finding the square of any number
btn_square = tk.Button(root, text="x\u00b2", command=lambda: add_to_calculation("**2"), width=5, font=("Arial", 14))
btn_square.grid(row=3, column=2,)

#for finding square root of any number
btn_sqrt = tk.Button(root, text="\u221a", command=lambda: add_to_calculation("**0.5"), width=5, font=("Arial", 14))
btn_sqrt.grid(row=3, column=3,)

#for division button
btn_div = tk.Button(root, text="\u00F7", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_div.grid(row=3, column=4)

#for digit 7
btn_1 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_1.grid(row=4, column=1)

#for digit 8
btn_2 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_2.grid(row=4, column=2)

#for digit 9
btn_3 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_3.grid(row=4, column=3)

#for multiplication
btn_mul = tk.Button(root, text="\u00d7", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_mul.grid(row=4, column=4)

#for digit 4
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=5, column=1)

#for digit 5
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=5, column=2)

#for digit 6
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=5, column=3)

#for subtraction
btn_min = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_min.grid(row=5, column=4)

#for digit 1
btn_7 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_7.grid(row=6, column=1)

#for digit 2
btn_8 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_8.grid(row=6, column=2)

#for digit 3
btn_9 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_9.grid(row=6, column=3)

#for addition
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=6, column=4)

#for digit 0
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=7, column=2)

#for decimal calculation
btn_decimal = tk.Button(root, text=".", command=lambda: add_to_calculation("."), width=5, font=("Arial", 14))
btn_decimal.grid(row=7, column=1)

#for getting the result of calculation
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=12, font=("Arial", 14), bg="blue", fg="white")
btn_equals.grid(row=7, column=3, columnspan=2)

root.mainloop()