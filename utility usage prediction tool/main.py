import pandas as pd
from sklearn.linear_model import LinearRegression
import tkinter as tk
from tkinter import messagebox

# Load Data
def load_data():
    try:
        return pd.read_csv("utility_data.csv")
    except FileNotFoundError:
        messagebox.showerror("Error", "CSV file not found!")
        return None

# View Data
def view_data():
    data = load_data()
    if data is not None:
        text.delete(1.0, tk.END)
        text.insert(tk.END, data.to_string())

# Add Record
def add_record():
    try:
        month = int(month_entry.get())
        usage = float(usage_entry.get())

        new_data = pd.DataFrame({
            "Month": [month],
            "Usage": [usage]
        })

        new_data.to_csv(
            "utility_data.csv",
            mode="a",
            header=False,
            index=False
        )

        messagebox.showinfo(
            "Success",
            "Record Added Successfully!"
        )

        month_entry.delete(0, tk.END)
        usage_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Invalid Input!"
        )

# Predict Usage
def predict_usage():
    data = load_data()

    if data is not None:
        X = data[["Month"]]
        y = data["Usage"]

        model = LinearRegression()
        model.fit(X, y)

        future_month = int(
            future_month_entry.get()
        )

        prediction = model.predict(
            [[future_month]]
        )

        result_label.config(
            text=f"Predicted Usage: {prediction[0]:.2f}"
        )

# GUI Window
root = tk.Tk()
root.title("Utility Usage Prediction Tool")
root.geometry("700x600")

# Add Data Section
tk.Label(root, text="Month").pack()
month_entry = tk.Entry(root)
month_entry.pack()

tk.Label(root, text="Usage").pack()
usage_entry = tk.Entry(root)
usage_entry.pack()

tk.Button(
    root,
    text="Add Record",
    command=add_record
).pack(pady=5)

# View Data
tk.Button(
    root,
    text="View Data",
    command=view_data
).pack(pady=5)

# Prediction Section
tk.Label(
    root,
    text="Future Month"
).pack()

future_month_entry = tk.Entry(root)
future_month_entry.pack()

tk.Button(
    root,
    text="Predict Usage",
    command=predict_usage
).pack(pady=5)

result_label = tk.Label(
    root,
    text=""
)
result_label.pack()

# Data Display
text = tk.Text(
    root,
    height=20,
    width=80
)
text.pack(pady=10)

root.mainloop()