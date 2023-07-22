```python
import json
import os

def load_settings():
    """
    Load settings from a JSON file.
    """
    if os.path.exists('settings.json'):
        with open('settings.json', 'r') as file:
            settings = json.load(file)
    else:
        settings = {
            'response_speed': 1.0
        }
        save_settings(settings)
    return settings

def save_settings(settings):
    """
    Save settings to a JSON file.
    """
    with open('settings.json', 'w') as file:
        json.dump(settings, file)

def format_message(message_name, message_content):
    """
    Format a message for display in the chatbox.
    """
    return f"{message_name}: {message_content}\n"

def adjust_response_speed(speed):
    """
    Adjust the response speed of the chatbot.
    """
    settings = load_settings()
    settings['response_speed'] = speed
    save_settings(settings)
```