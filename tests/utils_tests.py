```python
import unittest
from src import utils

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.sample_text = "Hello, AI Chatbot!"

    def test_preprocess_text(self):
        processed_text = utils.preprocess_text(self.sample_text)
        self.assertEqual(processed_text, "hello, ai chatbot!")

    def test_postprocess_text(self):
        postprocessed_text = utils.postprocess_text(self.sample_text)
        self.assertEqual(postprocessed_text, "Hello, AI Chatbot!")

    def test_calculate_response_time(self):
        response_time = utils.calculate_response_time(self.sample_text, speed=1)
        self.assertTrue(isinstance(response_time, float))

    def test_validate_speed_setting(self):
        self.assertTrue(utils.validate_speed_setting(1))
        self.assertFalse(utils.validate_speed_setting(10))
        self.assertFalse(utils.validate_speed_setting(-1))

if __name__ == '__main__':
    unittest.main()
```
