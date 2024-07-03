from tkinter import *
from tkinter import messagebox

# Define an empty list to store tasks
user_tasks = []

# Function to display the to-do list
def display_tasks():
    if not user_tasks:
        task_display.delete(1.0, END)
        task_display.insert(END, "Your to-do list is empty.")
    else:
        task_display.delete(1.0, END)
        task_display.insert(END, "To-Do List:\n")
        for i, task in enumerate(user_tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            task_display.insert(END, f"{i}. {task['task']} ({status})\n")

# Function to add a task to the to-do list
def add_task():
    task_name = task_entry.get()
    if task_name:
        new_task = {"task": task_name, "completed": False}
        user_tasks.append(new_task)
        display_tasks()
        task_entry.delete(0, END)
    else:
        task_display.delete(1.0, END)
        task_display.insert(END, "Task name cannot be empty.")

# Function to mark a task as completed
def mark_completed():
    try:
        task_number = int(task_entry.get())
        if 1 <= task_number <= len(user_tasks):
            user_tasks[task_number - 1]["completed"] = True
            display_tasks()
            task_entry.delete(0, END)
        else:
            task_display.delete(1.0, END)
            task_display.insert(END, "Invalid task number. Please enter a valid task number.")
    except ValueError:
        task_display.delete(1.0, END)
        task_display.insert(END, "Please enter a valid task number.")

# Function to remove a task from the to-do list
def remove_task():
    try:
        task_number = int(task_entry.get())
        if 1 <= task_number <= len(user_tasks):
            removed_task = user_tasks.pop(task_number - 1)
            display_tasks()
            task_entry.delete(0, END)
        else:
            task_display.delete(1.0, END)
            task_display.insert(END, "Invalid task number. Please enter a valid task number.")
    except ValueError:
        task_display.delete(1.0, END)
        task_display.insert(END, "Please enter a valid task number.")

# Function to exit the application
def exit_app():
    root_window.destroy()

# Main GUI window
root_window = Tk()
root_window.title("To-Do List GUI")
root_window.geometry("380x300")

# GUI components
task_entry = Entry(root_window, width=35)
task_entry.grid(row=0, column=0, pady=5, padx=5, columnspan=2)

add_button = Button(root_window, text="Add Task", command=add_task, width=13)
add_button.grid(row=0, column=2, pady=5, padx=5)

display_button = Button(root_window, text="Display List", command=display_tasks, width=13)
display_button.grid(row=1, column=0, pady=5, padx=5)

mark_button = Button(root_window, text="Mark Completed", command=mark_completed, width=13)
mark_button.grid(row=1, column=1, pady=5, padx=5)

remove_button = Button(root_window, text="Remove Task", command=remove_task, width=13)
remove_button.grid(row=1, column=2, pady=5, padx=5)

task_display = Text(root_window, height=10, width=40, wrap=WORD)
task_display.grid(row=2, column=0, columnspan=3, pady=10, padx=10)

quit_button = Button(root_window, text="Exit", command=exit_app, width=13)
quit_button.grid(row=4, column=0, pady=10, padx=10, columnspan=3)

root_window.mainloop()  # Keeps the window open and responsive to user actions.
