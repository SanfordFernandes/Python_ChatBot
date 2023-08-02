# Creating GUI with tkinter
from tkinter import *
from chatapp import chatbot_response


def send():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#B4B4B4", font=("Comic Sans MS", 12))  # 442265
        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)


base = Tk()
base.title("CHATBOT - CSL")
base.geometry("480x852")
base.resizable(width=FALSE, height=FALSE)

# Create Chat window
ChatLog = Text(base, bd=5, bg="#333333", height=10, width=10, font="Arial", )
ChatLog.config(state=DISABLED)

# Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

# Create Button to send message
SendButton = Button(base, font=("Comic Sans MS", 12, 'bold'), text="Send", width=5, height=50,
                    bd=5, bg="#B4B4B4", activebackground="#62898E", fg="#8533B4",
                    command=send)

# Create the box to enter message
EntryBox = Text(base, bd=5, bg="#B4B4B4", width="10", height="5", font="Arial")
# EntryBox.bind("<Return>", send)

# Place all components on the screen
scrollbar.place(x=460, y=3, height=840)
ChatLog.place(x=3, y=3, height=795, width=452)
EntryBox.place(x=3, y=800, height=50, width=380)
SendButton.place(x=385, y=800, height=50)
base.mainloop()
