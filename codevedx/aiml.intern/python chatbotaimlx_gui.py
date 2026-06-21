import tkinter as tk
from tkinter import scrolledtext
import json

# FAQ Data Load
with open("faq_data.json", "r") as file:
    faq = json.load(file)

# Message Send Function
def send_message():
    user_message = entry.get().lower()

    if user_message == "":
        return

    chat_area.insert(tk.END, "You: " + user_message + "\n")

    if user_message in faq:
        bot_reply = faq[user_message]
    else:
        bot_reply = "Sorry, I don't understand that question."

    chat_area.insert(tk.END, "Bot: " + bot_reply + "\n\n")

    entry.delete(0, tk.END)

# Main Window
root = tk.Tk()
root.title("AI Helpdesk Chatbot")
root.geometry("600x500")

# Chat Area
chat_area = scrolledtext.ScrolledText(root, width=70, height=20)
chat_area.pack(pady=10)
# Input Box
entry = tk.Entry(root, width=50)
entry.pack(side=tk.LEFT, padx=10, pady=10)

# Send Button
send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(side=tk.LEFT)

root.mainloop()