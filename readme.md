# Telegram/ChatGPT Project

## Overview

This project is a Telegram bot integrated with ChatGPT, utilizing the `aiogram` library for handling Telegram API interactions. The bot is designed to process various commands and provide intelligent responses using the OpenAI API.

## Features

- Connects to ChatGPT for generating conversational responses.
- Implements at least 4 mandatory functionalities and 2 optional ones.
- Adheres to the [PEP8](https://peps.python.org/pep-0008/) coding standard.
- Designed to be fault-tolerant and robust.
- Utilizes the `aiogram` library for seamless Telegram API integration.
- Handles commands such as `/start`, `/random`, `/gpt`, `/talk`, and `/quiz`.
- Supports dynamic topic selection and quiz functionality with interactive buttons.
- Manages conversation flow using `FSMContext` for state management.

## Getting Started

### Prerequisites

- Python 3.x
- A Telegram bot token
- An OpenAI API key

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/maximkatut/telegram_bot.git
   cd telegram_bot
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables in a `.env` file:
   ```
   TELEGRAM_TOKEN=your_telegram_token_here
   OPENAI_TOKEN=your_openai_api_key_here
   ```

### Running the Bot

To start the bot, run:

```bash
python main.py
```

## Deployment

The project can be deployed on various platforms such as ngrok, pythonanywhere, or glitch.

## Additional Features

- Utilizes `FSMContext` for managing complex conversations and state transitions.
- Environment variables are used for storing sensitive information like tokens.
- Includes logging for better traceability and debugging.
- The project can be extended with technologies not covered in the first module.
- Implements a quiz feature with dynamic topic selection and scoring.

## Contribution

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
