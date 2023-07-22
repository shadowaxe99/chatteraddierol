```python
import tkinter as tk
from src.settings import Settings

class SettingsUI:
    def __init__(self, master):
        self.master = master
        self.settings = Settings()

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.response_speed_label = tk.Label(self.frame, text="Response Speed")
        self.response_speed_label.pack()

        self.response_speed_slider = tk.Scale(self.frame, from_=1, to=10, orient=tk.HORIZONTAL)
        self.response_speed_slider.set(self.settings.get_response_speed())
        self.response_speed_slider.pack()

        self.save_button = tk.Button(self.frame, text="Save", command=self.save_settings)
        self.save_button.pack()

    def save_settings(self):
        self.settings.set_response_speed(self.response_speed_slider.get())
        self.settings.save()
        self.master.destroy()
```