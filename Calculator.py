import tkinter as tk

# Function to handle number/operator button clicks
def click(event):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + event.widget["text"])

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression and display the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Initialize the main application window
root = tk.Tk()
root.title("Manoj's Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry widget for displaying input and results
entry = tk.Entry(
    root,
    font=("Arial", 20),
    borderwidth=2,
    relief="solid",
    justify="right"
)
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Frame to hold all calculator buttons
btn_frame = tk.Frame(root)
btn_frame.pack()

# Layout for calculator buttons (each sublist is a row)
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

# Dynamically create and place buttons
for row in buttons:
    row_frame = tk.Frame(btn_frame)
    row_frame.pack(expand=True, fill="both")

    for char in row:
        btn = tk.Button(
            row_frame,
            text=char,
            font=("Arial", 18),
            width=5,
            height=2
        )
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

        # Assign appropriate functionality
        if char == 'C':
            btn.config(command=clear)
        elif char == '=':
            btn.config(command=calculate)
        else:
            btn.bind("<Button-1>", click)

# Start the main event loop
root.mainloop()
