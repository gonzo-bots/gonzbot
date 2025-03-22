GonzBot

GonzBot is a Python-based Discord bot that integrates REST APIs, ChatGPT, and sentiment analysis to deliver AI-driven interactions and personalized gaming statistics, deployed via Docker and AWS for real-world cloud experience.
Features

    AI Integration: Utilizes ai.py for artificial intelligence capabilities.​
    Sentiment Analysis: Incorporates sentimentanalysis.py to assess text sentiment.​
    Steam API Interaction: Employs steamapi.py to fetch data from the Steam platform.​

Installation

    Clone the repository:

git clone https://github.com/gonzo-bots/gonzbot.git
cd gonzbot

Create and activate a virtual environment:

python3 -m venv env
source env/bin/activate  # On Windows, use 'env\Scripts\activate'

Install dependencies:

    pip install -r requirements.txt

Usage

After installation, you can run the bot using the following command:​

python gonzobot.py

Ensure you have configured any necessary API keys or environment variables required by the bot. Refer to the code and comments within gonzobot.py for specific configurations.​
Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the project.​
License

This project is licensed under the MIT License. See the LICENSE file for details.
