```python
import unittest
from src.settings import Settings

class TestSettings(unittest.TestCase):

    def setUp(self):
        self.settings = Settings()

    def test_initial_speed(self):
        self.assertEqual(self.settings.get_response_speed(), 1)

    def test_set_speed(self):
        self.settings.set_response_speed(0.5)
        self.assertEqual(self.settings.get_response_speed(), 0.5)

    def test_invalid_speed(self):
        with self.assertRaises(ValueError):
            self.settings.set_response_speed(2)

if __name__ == '__main__':
    unittest.main()
```