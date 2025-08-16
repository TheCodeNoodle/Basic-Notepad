import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog

root = ctk.CTk()
root.title("Notepad")
root.geometry("800x600")
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

current_file = None
untitled_count = 1  # counter for Untitled docs

def new_file():
    global current_file, untitled_count
    text_area.delete("1.0", "end")   # clear textbox
    current_file = None
    root.title(f"Notepad - Untitled {untitled_count}")
    untitled_count += 1

def save_file():
    global current_file, untitled_count
    text = text_area.get("1.0", "end-1c")  # get text (without trailing newline)

    if current_file is None:
        # file not saved yet → ask for name, suggest Untitled N
        file_path = filedialog.asksaveasfilename(
            initialfile=f"Untitled {untitled_count}.txt",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not file_path:  # user canceled
            return
        current_file = file_path

    with open(current_file, "w", encoding="utf-8") as file:
        file.write(text)

    root.title(f"Notepad - {current_file.split('/')[-1]}")  # show file name in title
    print(f"Saved to {current_file}")

def open_file():
    global current_file
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        text_area.delete("1.0", "end")
        text_area.insert("1.0", text)
        current_file = file_path
        root.title(f"Notepad - {file_path.split('/')[-1]}")
        print(f"Opened {file_path}")


file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit")

text_area = ctk.CTkTextbox(root, wrap="word", undo=True, fg_color="#252526", text_color="#F1F1F1", corner_radius=0)
text_area.pack(expand=True, fill="both")


root.mainloop()