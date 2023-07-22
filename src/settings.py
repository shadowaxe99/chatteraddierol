```python
class Settings:
    def __init__(self):
        # Default response speed is set to medium
        self.response_speed = 'medium'

    def get_response_speed(self):
        return self.response_speed

    def set_response_speed(self, speed):
        if speed in ['slow', 'medium', 'fast']:
            self.response_speed = speed
        else:
            raise ValueError("Invalid speed. Please choose from 'slow', 'medium', or 'fast'.")

    def to_dict(self):
        return {
            'response_speed': self.response_speed
        }

    @staticmethod
    def from_dict(settings_dict):
        settings = Settings()
        settings.set_response_speed(settings_dict.get('response_speed', 'medium'))
        return settings
```