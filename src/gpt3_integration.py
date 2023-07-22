```python
import openai
from settings import Settings

class GPT3Integration:
    def __init__(self):
        self.settings = Settings()
        openai.api_key = self.settings.get_api_key()

    def generate_response(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=self.settings.get_response_speed(),
            max_tokens=150
        )
        return response.choices[0].text.strip()

    def update_settings(self, new_settings):
        self.settings = new_settings
        openai.api_key = self.settings.get_api_key()
```