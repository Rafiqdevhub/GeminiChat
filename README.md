# GeminiChat: Your AI Companion

A conversational AI chatbot built with Streamlit and Google's Gemini AI models.

![GeminiChat](https://img.shields.io/badge/GeminiChat-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.7+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

GeminiChat is a web-based AI assistant that leverages Google's Gemini AI models to provide intelligent, conversational responses. Built with Streamlit, it offers a clean and interactive user interface for seamless AI conversation.

## Features

- 🤖 Integration with Google's Gemini AI models (gemini-2.0-flash and gemini-2.0)
- 🎛️ Adjustable temperature setting to control response creativity
- 🔄 Option to clear chat history
- 💬 Persistent chat session during app usage
- 📱 Responsive design with Streamlit's wide layout

## Installation

1. Clone this repository:
   ```
   git clone 
   cd 
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

   You can obtain a Google API key from the [Google AI Studio](https://makersuite.google.com/app/apikey).

## Usage

Run the application with:
```
streamlit run app.py
```

Then access the application in your web browser at `http://localhost:8501`.

## Requirements

- Python 3.7+
- streamlit==1.32.0
- google-generativeai==0.3.2
- python-dotenv==1.0.0
