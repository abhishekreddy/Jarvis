import tkinter as tk
import os
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from ProcessSentence import ProcessSentence

BOT_NAME = "Jarvis"
USER_NAME = "Ananymous"
CHAT_HEIGHT = 10
CHAT_WIDTH  = 60
COMMENT_HEIGHT = 2
COMMENT_WIDTH = 60
DISABLED   = 'disabled'
NORMAL = 'normal'
READONLY = 'readonly'
BUTTON_TEXT = "Send"
ORIENT_VERTICAL='vertical'
ORIENT_HORIZONTAL='horizontal'
RIGHTSIDE = 'right'
LEFT = 'left'
TOP = 'top'
BOTTOM = 'bottom'



class Visual(tk.Frame):
    """This class represents visual bot"""

    botname = BOT_NAME
    username = USER_NAME

    def __init__(self, *args):
        tk.Frame.__init__(self, *args)
        self.label = tk.Label(self, text = self.botname)
        self.label.pack()
        self.chat  = ScrolledText(self, wrap = WORD, state = DISABLED, height = CHAT_HEIGHT, width = CHAT_WIDTH)
        self.chat.pack()
        self.comment = tk.Text(self, wrap = WORD, height = COMMENT_HEIGHT, width = COMMENT_WIDTH)
        self.comment.pack()
        self.button = tk.Button(self, text = BUTTON_TEXT, command= self.button_callback)
        self.button.pack()

        self.talk = ProcessSentence()

    def button_callback(self):
        text = self.comment.get("1.0", END)
        self.update_chat(self.talk.get_user_name(), text)
        text.rstrip(os.linesep)
        responce = self.talk.check_for_greeting(text)
        if responce:
            self.update_chat(self.talk.get_bot_name(), responce + '\n')

    def update_chat(self, name, text):
        self.chat.configure(state = NORMAL)
        self.chat.insert('end', name + " : ", 'GREEN')
        self.chat.tag_config('GREEN', foreground='GREEN')
        self.chat.insert('end', text)
        self.chat.see(END)
        self.chat.configure(state = DISABLED)
