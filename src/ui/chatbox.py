```python
import tkinter as tk
from tkinter import ttk, scrolledtext

class ChatboxUI:
    def __init__(self, root):
        self.root = root
        self.chat_history = scrolledtext.ScrolledText(self.root, state='disabled')
        self.user_input = tk.Entry(self.root)
        self.send_button = ttk.Button(self.root, text="Send")
        self.settings_button = ttk.Button(self.root, text="Settings")
        self._place_widgets()

    def _place_widgets(self):
        self.chat_history.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.user_input.grid(row=1, column=0, sticky='nsew')
        self.send_button.grid(row=1, column=1, sticky='nsew')
        self.settings_button.grid(row=0, column=2, sticky='nsew')

    def append_message(self, message, sender):
        self.chat_history.configure(state='normal')
        self.chat_history.insert(tk.END, f"{sender}: {message}\n")
        self.chat_history.configure(state='disabled')

    def clear_input(self):
        self.user_input.delete(0, tk.END)

    def get_input(self):
        return self.user_input.get()

    def set_send_button_command(self, command):
        self.send_button.configure(command=command)

    def set_settings_button_command(self, command):
        self.settings_button.configure(command=command)
```