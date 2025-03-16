# Project "Telegram/ChatGPT"

## Conditions:

- The project should be a Telegram bot connected to ChatGPT.

- The project must implement functionalities from 4 mandatory points and 2 optional points.

- The project code must comply with the [PEP8](https://peps.python.org/pep-0008/) standard.

- The code should be fault-tolerant.

- Any library for the Telegram API is allowed.

### OpenAI Token

The key for the entire group should be requested from the curator in Pumble.

### How to submit the project?

In the chat, there will be a link to a form where you need to add your Name (as in Pumble) and a link to GitHub.

> Important! If you publish the OpenAI token on GitHub, it will be automatically revoked/blocked within 10-15 minutes.

### Bonus points if the project includes:

- A README file
- A requirements.txt file
- Use of ConversationHandler
- Use of environment variables (for storing tokens)
- Logging
- Deployment of the project on a server (ngrok, pythonanywhere, glitch, or others)
- Use of technologies not covered in the first module

### Project consultations

Three lectures are allocated for answering questions and reviews.

They can be used consecutively all at once or divided into parts. For example:

- Conduct 2 lectures,
- Start module 2, lectures 1 and 2 (they are theoretical),
- Then conduct the final lecture on the project.

### Implementation assistance

1. Issuing the OpenAI token for the group. For tests, use the cheaper version: gpt 3.5 or GPT-4o mini.
2. There is a prepared project template, which will be reviewed in the first lecture.
3. In the first lecture, the first steps of work will be shown. Implementation of tasks 1 and 2. Further independent work.

---

# Tasks

## Mandatory

### 1. _"Random Fact"_

The Telegram bot should handle the /random command.
When processing the command, it sends a pre-prepared image
and makes a request to ChatGPT with a pre-prepared prompt.
The ChatGPT response should be received and sent to the user.
The message should have an attached "Finish" button, which works the same as the /start command when pressed.
And a "Want another fact" button, which works the same as the /random command when pressed.

### 2. _"ChatGPT Interface"_

The Telegram bot should handle the /gpt command.
When processing the command, it sends a pre-prepared image
and makes a request to ChatGPT, passing the text of the received message. The ChatGPT response should be received and sent to the user as a text message.

### 3. _"Dialogue with a Famous Person"_

The Telegram bot should handle the /talk command.
When processing the command, the bot sends a pre-prepared image and
offers a choice of several famous personalities using buttons. By pressing a button, the prompt of the selected personality should be set.
Further text messages from the user should be passed to ChatGPT and
its responses returned to the user.
They should have an attached "Finish" button, which works the same as the /start command when pressed.

### 4. _"Quiz"_

The Telegram bot should handle the /quiz command.
When processing the command, the bot sends a pre-prepared image
and offers a choice of several topics using buttons.
After selecting a topic, send a request to ChatGPT and, after receiving a quiz question, send it to the user. The next text message from the user is considered an answer.
It should be sent to ChatGPT and the result received. The result should be sent to the user
with the option to ask another question on the same topic, change the topic, or finish the quiz using buttons.
The bot should also keep track of the number of correct answers and
display it along with the next result.

### 5. **Optional Topic** (optional)

Choose two or more ideas from the suggested ones (or come up with your own!):

**"Translator"**

The bot offers to choose a language to translate the text into using buttons.
After selecting a language, the user sends the text to be translated.
The bot uses ChatGPT to translate the text and sends the result to the user.
The message should have an attached button to change the language and a "Finish" button, which works the same as the /start command when pressed.

**"Voice ChatGPT"**

The bot should accept a voice message from the user. Convert it to text
and send it to ChatGPT. After receiving a response, convert it to a voice message and
send it as an audio message to the user.

**"Movie and Book Recommendations"**

The bot offers to choose a category of recommendations: movies, books, music.
After selecting a category, the bot asks for a genre.
After receiving it, it forms a request and asks ChatGPT for recommendations
and sends them to the user.
They should have attached buttons:

"Don't like", which makes the selected work uninteresting. Pressing the
button generates a new response, taking into account all uninteresting works entered by the user.

"Finish", which works the same as the /start command when pressed.

**"Vocabulary Trainer"**

The bot helps the user expand their foreign language vocabulary.
It can send a new word with a translation and usage examples.
When sending, the word is considered learned. The message should have
attached buttons "Another word", "Practice", and "Finish".
By pressing "Practice", the bot should conduct a test on learned words
with validation from ChatGPT.

The test should involve iterating over all learned words. Each such word
should be displayed in a message. The next user message is considered
the translation of this word. For validation of correctness, ChatGPT can be used.
At the end of the test, the result should be displayed as the number of correct answers.

**"Image Recognition"**

The bot should accept an image from the user and pass it to ChatGPT.
ChatGPT should determine what is in the image and describe it in text form.
The response should be sent to the user as a text message.

**"Resume Assistance"**

The bot asks the user for information about education, work experience, and skills.
Based on the received data, the bot generates a resume template and sends it to the user.

#### Your Own Topic

If you have an idea that you want to implement in the project, it can replace
one of the optional points. For validation, contact the Mentor.
