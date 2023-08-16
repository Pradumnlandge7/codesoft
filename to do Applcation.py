import tkinter as tk
from tkinter import messagebox

class TodoListApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application 🔏")

        self.tasks = []

        self.task_entry = tk.Entry(root, width=80)
        self.task_entry.grid(row=0, column=0, padx=10, pady=30)

        self.add_button = tk.Button(root, text="Add Your Fev Task", command=self.add_task, bg='blue')
        self.add_button.grid(row=0, column=1, padx=5, pady=10,)

        self.task_listbox = tk.Listbox(root, width=50, height=10,  bg = "grey", fg = "white")
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg='red')
        self.delete_button.grid(row=2, column=1, padx=10, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["completed"] else " "
            self.task_listbox.insert(tk.END, f"[{status}] {task['task']}")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_task_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApplication(root)
    root.mainloop()
