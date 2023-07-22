```python
import unittest
from unittest.mock import patch
from src.gpt3_integration import GPT3Integration

class TestGPT3Integration(unittest.TestCase):

    def setUp(self):
        self.gpt3_integration = GPT3Integration()

    @patch('src.gpt3_integration.openai.ChatCompletion.create')
    def test_generate_response(self, mock_chat_completion):
        mock_chat_completion.return_value = {
            'choices': [{'message': {'role': 'system', 'content': 'Test response'}}]
        }

        user_message = "Hello, how are you?"
        response = self.gpt3_integration.generate_response(user_message)
        self.assertEqual(response, "Test response")

    @patch('src.gpt3_integration.openai.ChatCompletion.create')
    def test_generate_response_with_context(self, mock_chat_completion):
        mock_chat_completion.return_value = {
            'choices': [{'message': {'role': 'system', 'content': 'I am fine, thank you.'}}]
        }

        user_message = "Hello, how are you?"
        context = "The user greeted the bot."
        response = self.gpt3_integration.generate_response(user_message, context)
        self.assertEqual(response, "I am fine, thank you.")

if __name__ == '__main__':
    unittest.main()
```