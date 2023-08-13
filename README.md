# Blog Content Generator App

Live version of this app [blog-content-generator.streamlit.app](https://blog-content-generator-6simuukxnb.streamlit.app/)

## Features
- Generates blog-style texts using Cohere API's Large Language Model based on user prompts.
- User can customize the tone and creativity parameters to shape the generated content.
- Receive contextually relevant content that fits the given prompt and instructions.

## Description

- The text prompt form accepts a Tone as well as a Creativity parameter.
- The app then generates a prompt with an instruction to write a respective text and sends a request to the Cohere API including the constructed prompt, tone, and creativity parameters.
- The Cohere API processes this input using one of their LLM models trained on a vast amount of publicly available text content.
- It predicts the next likely word tokens based on the input prompt and generates blog-style content accordingly.
- Then, the app displays the generated content to the user through the Streamlit user interface.

## Installation and Usage
1. Clone the repository:

```bash
git clone https://github.com/your-username/blog-content-generator.git

```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run content_generator.py
```
