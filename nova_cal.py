
import tkinter as tk
import math

root = tk.Tk()
root.title("NovaCalc - Scientific Calculator")
root.geometry("380x550")
root.configure(bg="#222222")
root.resizable(False, False)

expression = ""

def press(value):
    global expression
    expression += str(value)
    display_var.set(expression)

def clear():
    global expression
    expression = ""
    display_var.set("")

def delete():
    global expression
    expression = expression[:-1]
    display_var.set(expression)

def calculate():
    global expression
    try:
        allowed = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt,
            "log": math.log10,
            "ln": math.log,
            "pi": math.pi,
            "e": math.e,
            "factorial": math.factorial
        }

        result = eval(expression.replace("^", "**"),
                      {"__builtins__": None}, allowed)

        expression = str(result)
        display_var.set(expression)

    except Exception:
        display_var.set("Error")
        expression = ""

display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 22),
    bg="#333333",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="white"
)
display.pack(fill="x", padx=15, pady=20, ipady=18)

buttons = [
    ["sin", "cos", "tan", "C"],
    ["sqrt", "log", "ln", "DEL"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "^", "+"],
    ["(", ")", "pi", "e"],
    ["="]
]

for row in buttons:
    frame = tk.Frame(root, bg="#222222")
    frame.pack(expand=True, fill="both", padx=10)

    for item in row:
        if item == "=":
            btn = tk.Button(
                frame, text=item, font=("Arial", 16),
                bg="#555555", fg="white",
                command=calculate
            )
            btn.pack(side="left", expand=True, fill="both", padx=4, pady=4)
            continue

        if item == "C":
            action = clear
        elif item == "DEL":
            action = delete
        elif item in ["sin", "cos", "tan", "sqrt", "log", "ln"]:
            action = lambda x=item: press(x + "(")
        elif item == "pi":
            action = lambda: press("pi")
        elif item == "e":
            action = lambda: press("e")
        else:
            action = lambda x=item: press(x)

        btn = tk.Button(
            frame,
            text=item,
            font=("Arial", 13),
            bg="#444444",
            fg="white",
            activebackground="#666666",
            activeforeground="white",
            bd=0,
            command=action
        )
        btn.pack(side="left", expand=True, fill="both", padx=4, pady=4)

root.mainloop()
