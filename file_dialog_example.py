import tkinter as tk
from tkinter import filedialog
print("Hello hello")
root = tk.Tk()  # fire up the GUI
root.withdraw()  # hide main window
file_path = filedialog.askopenfilename()  # pop up dialog
print(f"Your file path is {file_path}")
