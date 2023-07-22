```python
import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from src.ui.chatbox import Chatbox
from src.ui.settings_ui import SettingsUI

app = QApplication([])

class TestUI(unittest.TestCase):
    def setUp(self):
        self.chatbox = Chatbox()
        self.settings_ui = SettingsUI()

    def test_chatbox_ui(self):
        self.assertTrue(self.chatbox.isVisible())
        self.assertEqual(self.chatbox.user_input.text(), "")
        self.assertEqual(self.chatbox.chat_history.toPlainText(), "")
        QTest.keyClicks(self.chatbox.user_input, 'Hello, chatbot!')
        QTest.mouseClick(self.chatbox.send_button, Qt.LeftButton)
        self.assertEqual(self.chatbox.user_input.text(), "")

    def test_settings_ui(self):
        self.assertTrue(self.settings_ui.isVisible())
        self.assertEqual(self.settings_ui.response_speed_slider.value(), 50)
        QTest.mouseClick(self.settings_ui.settings_button, Qt.LeftButton)
        self.settings_ui.response_speed_slider.setValue(70)
        self.assertEqual(self.settings_ui.response_speed_slider.value(), 70)

if __name__ == '__main__':
    unittest.main()
```