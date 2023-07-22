# AI Chatbot with GPT-3.5 Turbo Integration

This software is an AI-powered chatbot that integrates with GPT-3.5 Turbo. It is capable of responding to user input with contextual awareness, allowing for natural and interactive conversations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)

## Installation

1. Ensure you have Python installed on your system. If not, download and install Python from the official website.

2. Clone this repository to your local machine.

    ```
    git clone https://github.com/your-repo/ai-chatbot.git
    ```

3. Navigate to the project directory.

    ```
    cd ai-chatbot
    ```

4. Install the required dependencies.

    ```
    pip install -r requirements.txt
    ```

5. Run the main script to start the chatbot.

    ```
    python src/main.py
    ```

## Usage

1. The chatbot interface is presented in a chatbox UI where users can input messages and view the chat history.

2. The chatbot uses GPT-3.5 Turbo API to process user queries and generate context-aware responses.

3. Users can adjust the chatbot's response speed through configurable settings in the settings UI.

## Testing

1. Navigate to the tests directory.

    ```
    cd tests
    ```

2. Run the test scripts.

    ```
    python chatbot_tests.py
    python gpt3_integration_tests.py
    python ui_tests.py
    python settings_tests.py
    python utils_tests.py
    ```

## Troubleshooting

If you encounter any issues while installing or running the software, please check the following:

1. Ensure you have the correct version of Python installed.

2. Make sure all dependencies are installed. You can do this by running `pip install -r requirements.txt` in the project directory.

3. If the chatbot is not responding as expected, ensure that the GPT-3.5 Turbo API is correctly integrated and functioning.

For further assistance, please raise an issue in the repository.