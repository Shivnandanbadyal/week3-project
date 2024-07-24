import csv
import os
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename='expenses.csv'):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Category', 'Description', 'Amount'])

    def add_expense(self, date, category, description, amount):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, description, amount])

    def get_expenses(self):
        expenses = []
        with open(self.filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
        return expenses

    def get_summary(self):
        expenses = self.get_expenses()
        summary = {}
        for expense in expenses:
            category = expense['Category']
            amount = float(expense['Amount'])
            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount
        return summary

class ExpenseTrackerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        # User input fields
        self.date_label = tk.Label(root, text="Date (YYYY-MM-DD)")
        self.date_label.grid(row=0, column=0)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=0, column=1)

        self.category_label = tk.Label(root, text="Category")
        self.category_label.grid(row=1, column=0)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=1, column=1)

        self.description_label = tk.Label(root, text="Description")
        self.description_label.grid(row=2, column=0)
        self.description_entry = tk.Entry(root)
        self.description_entry.grid(row=2, column=1)

        self.amount_label = tk.Label(root, text="Amount")
        self.amount_label.grid(row=3, column=0)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=3, column=1)

        self.add_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=4, column=0, columnspan=2)

        self.summary_button = tk.Button(root, text="Show Summary", command=self.show_summary)
        self.summary_button.grid(row=5, column=0, columnspan=2)

    def add_expense(self):
        date = self.date_entry.get()
        category = self.category_entry.get()
        description = self.description_entry.get()
        amount = self.amount_entry.get()
        try:
            datetime.strptime(date, '%Y-%m-%d')
            tracker.add_expense(date, category, description, float(amount))
            messagebox.showinfo("Success", "Expense added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please check the date and amount.")

    def show_summary(self):
        summary = tracker.get_summary()
        summary_text = "\n".join([f"{category}: ${amount:.2f}" for category, amount in summary.items()])
        messagebox.showinfo("Expense Summary", summary_text)

if __name__ == "__main__":
    tracker = ExpenseTracker()
    root = tk.Tk()
    app = ExpenseTrackerUI(root)
    root.mainloop()