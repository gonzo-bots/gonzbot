GonzBot



A powerful Discord bot built with Python, Docker, and AWS, integrating Counter-Strike stats, AI chat capabilities, and sentiment analysis.
Features

    Counter-Strike Stats Lookup – Fetch real-time game statistics via the Steam API.
    ChatGPT Integration – Chat directly with AI within Discord.
    Sentiment Analysis – Analyze chat history using VADER for emotional insights.
    Cloud Deployment – Hosted on AWS ECS, with Dockerized deployment.
    CI/CD Automation – Streamlined updates with GitHub Actions and AWS ECR.
    Secure API Key Management – Credentials stored securely in AWS Secrets Manager.

Installation
Prerequisites

    Python 3.9+
    Docker
    AWS CLI (for deployment)
    Git

Setup

    Clone the repository

git clone https://github.com/gonzo-bots/gonzbot.git
cd gonzbot

Create a virtual environment and install dependencies

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt

Set up environment variables

    Create a .env file and add your API keys:

    DISCORD_TOKEN=your_discord_token
    STEAM_API_KEY=your_steam_api_key
    OPENAI_API_KEY=your_openai_api_key
    AWS_SECRET_NAME=your_secret_name
    AWS_REGION=your_aws_region

Run the bot locally

    python bot.py

 Docker Deployment
Build & Run Locally

docker build -t gonzbot .
docker run --env-file .env -d gonzbot

Deploy to AWS ECS

    Authenticate with AWS ECR

aws ecr get-login-password --region YOUR_AWS_REGION | docker login --username AWS --password-stdin YOUR_ECR_URL

Push to ECR

    docker tag gonzbot:latest YOUR_ECR_URL/gonzbot:latest
    docker push YOUR_ECR_URL/gonzbot:latest

    Deploy to ECS (Using pre-configured task definition)

 Usage

    Use /stats <Steam ID> to fetch Counter-Strike stats.
    Use /chat <prompt> to chat with AI.
    Use /sentiment to analyze recent chat history.


Contributions are welcome! Feel free to open issues and pull requests.
Contact

    Author: Brandon Wester
    GitHub: @BrandonWester
    LinkedIn: Brandon Wester
