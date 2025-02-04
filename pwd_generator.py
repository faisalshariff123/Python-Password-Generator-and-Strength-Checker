import random
import sys
import tkinter as tk

# functions
def generate():
    global pwd
    if choice_A.get() == "Y":
        pwd = ""  # Reset password to avoid appending each time
        for i in range(x):
            random_char = random.choice(characters)
            pwd += random_char
        result_label.config(text=f"Generated Password: {pwd}")
        
    if choice_A.get() == "N":
        result_label.config(text="Exiting Program...")
        sys.exit()

def strength():
    global pwd
    if choice_A.get() == "Y" and choice_B.get() == "Y":
        found_special = False
        for i in special:
            if i in pwd:
                found_special = True
                result_label.config(text="Strong Password!")
                break
        if not found_special:
            result_label.config(text="Weak Password!")
    if choice_A.get() == "N" or choice_B.get() == "N":
        result_label.config(text="Exiting Program...")
        sys.exit()
        
def reset():
    global pwd
    result_label.config(text="")
    pwd = ""
    choice_A.delete(0, tk.END)
    choice_B.delete(0, tk.END)

def exit_program():
    sys.exit()

# variables    
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
special = '!@#$%^&*()'
x = random.randint(8,16)
pwd = ""

# application window
app = tk.Tk()
app.title("Password Generator")
app.geometry("600x300")

# frame
frame = tk.Frame(app)
frame.grid(row=0, column=0, padx=10, pady=10)

# choice to generate random password
label_A = tk.Label(frame, text="Do you want to generate random password? (Y/N):")
label_A.grid(row=0, column=0, padx=5, pady=5)
choice_A = tk.Entry(frame)
choice_A.grid(row=0, column=1, padx=5, pady=5)

# choice to check password strength
label_B = tk.Label(frame, text="Do you want to check for password strength? (Y/N):")
label_B.grid(row=1, column=0, padx=5, pady=5)
choice_B = tk.Entry(frame)
choice_B.grid(row=1, column=1, padx=5, pady=5)

# button to generate password
button_A = tk.Button(frame, text="Generate password", command=generate)
button_A.grid(row=2, column=0, columnspan=2, pady=5)

# button to check password strength
button_B = tk.Button(frame, text="Check password strength", command=strength)
button_B.grid(row=3, column=0, columnspan=2, pady=5)

# button to reset
button_C = tk.Button(frame, text="Reset", command=reset)
button_C.grid(row=4, column=0, columnspan=2, pady=5)

# button to exit program
exit_button = tk.Button(frame, text="Exit", command=exit_program)
exit_button.grid(row=5, column=0, columnspan=2, pady=5)

# label to display the result
result_label = tk.Label(app, text="", font=("Arial", 14))
result_label.grid(row=1, column=0, columnspan=2, pady=10)

# Start the GUI loop
app.mainloop()
