README!

# NewsAI

NewsAI is a Discord bot that can provide summaries of news articles based on user requests.

## Prerequisites

To run NewsAI, you will need to have the following installed on your machine:

- Python 3.6 or higher
- pip

## Installation

1. Clone the NewsAI repository to your local machine.

2. In the root directory of the repository, create a file called `.env` and include the following environment variables:

# Discord bot token
DISCORD_TOKEN=<your Discord bot token>

# OpenAI API key
OPENAI_API_KEY=<your OpenAI API key>

# News API key
NEWS_API_KEY=<your News API key>


3. Replace the values for the environment variables with your own keys. You can obtain a Discord bot token by creating a new bot application in the Discord Developer Portal. You can obtain an OpenAI API key by creating an account on the OpenAI website and generating an API key. You can obtain a News API key by creating an account on the News API website and generating an API key.

4. Install the required Python packages by running the following command in the root directory of the repository: pip install -r requirements.txt


## Usage

To run NewsAI, run the following command in the root directory of the repository: python NewsAI.py


Once the bot is running, you can interact with it on Discord using the `$news` command. You can provide the bot with the number of articles you want to retrieve and the topic you want to retrieve articles for. For example, to retrieve 5 articles about technology, you can type:


$news 5 technology
The bot will retrieve the top 5 headlines related to the topic and provide a summary of each article. 




