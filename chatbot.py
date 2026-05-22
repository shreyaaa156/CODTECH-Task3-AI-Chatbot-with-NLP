import nltk
from nltk.chat.util import Chat, reflections

pairs = [

[
r"hi|hello|hey",
["Hello! How can I help you today?"]
],

[
r"what is your name ?",
["I am an AI chatbot created using Python and NLTK."]
],

[
r"how are you ?",
["I am functioning properly."]
],

[
r"what can you do ?",
["I can answer basic questions and chat with users."]
],

[
r"(.*) your creator ?",
["I was created as part of a CODTECH internship task."]
],

[
r"bye",
["Goodbye! Have a nice day."]
]

]

chatbot = Chat(pairs, reflections)

print("AI Chatbot Started")
print("Type 'bye' to exit\n")

chatbot.converse()