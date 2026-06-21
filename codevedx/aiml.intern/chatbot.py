import json

# FAQ data load karo
with open("faq_data.json", "r") as file:
    faq = json.load(file)

print("🤖 AI Helpdesk Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in faq:
        print("Bot:", faq[user_input])
    else:
        print("Bot: Sorry, I don't understand that question.")

    if user_input == "bye":
        break

    