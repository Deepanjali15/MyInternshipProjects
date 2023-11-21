import tkinter as tk
from tkinter import ttk

class Task:
    def __init__(self, description, due_date=None, priority=None):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List Application")

        self.tasks = []
        self.completed_tasks = []

        self.create_box()

    def create_box(self):
        # Task Entry Frame
        entry_frame = ttk.Frame(self.master, padding="10")
        entry_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(entry_frame, text="Task Description:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.description_entry = ttk.Entry(entry_frame, width=30)
        self.description_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(entry_frame, text="Due Date (optional):").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.due_date_entry = ttk.Entry(entry_frame, width=30)
        self.due_date_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        ttk.Label(entry_frame, text="Priority (optional):").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.priority_entry = ttk.Entry(entry_frame, width=30)
        self.priority_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        add_button = ttk.Button(entry_frame, text="Add Task", command=self.add_task)
        add_button.grid(row=3, column=1, pady=10)

        # Task List Frame
        list_frame = ttk.Frame(self.master, padding="10")
        list_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.task_listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE, width=40, height=10)
        self.task_listbox.grid(row=0, column=0, padx=5, pady=5)

        self.display_tasks()

        mark_complete_button = ttk.Button(list_frame, text="Mark as Completed", command=self.mark_completed)
        mark_complete_button.grid(row=1, column=0, pady=5)

        update_button = ttk.Button(list_frame, text="Update Task", command=self.update_task)
        update_button.grid(row=2, column=0, pady=5)

        remove_button = ttk.Button(list_frame, text="Remove Task", command=self.remove_task)
        remove_button.grid(row=3, column=0, pady=5)

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Pending"
            task_info = f"{index}. {task.description} - Due: {task.due_date} - Priority: {task.priority} - Status: {status}"
            self.task_listbox.insert(tk.END, task_info)

    def add_task(self):
        description = self.description_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()

        new_task = Task(description, due_date, priority)
        self.tasks.append(new_task)
        self.display_tasks()

        # Clear entry fields after adding a task
        self.description_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.tasks[task_index].completed = True
            self.completed_tasks.append(self.tasks.pop(task_index))
            self.display_tasks()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            new_description = self.description_entry.get()
            new_due_date = self.due_date_entry.get()
            new_priority = self.priority_entry.get()

            task = self.tasks[task_index]
            task.description = new_description
            task.due_date = new_due_date
            task.priority = new_priority

            self.display_tasks()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            removed_task = self.tasks.pop(task_index)
            self.display_tasks()
            print(f"Task '{removed_task.description}' removed.")


def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
