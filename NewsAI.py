import requests
import json
import openai
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='$', intents=intents)

news_api_key = os.getenv('NEWS_API_KEY')
openai.api_key = os.getenv('OPENAI_API_KEY')
news_url = "https://newsapi.org/v2/top-headlines"


def summarize_article(url):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=(f"Please summarize this article: {url}"),
        max_tokens=512,
        n=1,
        stop=None,
        temperature=0.5,
    )

    summary = response.choices[0].text.strip()
    return summary


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user} and ready to provide some news!')


@bot.event
async def on_message(message):
    if message.content.startswith('$news'):
        # Get the number of articles the user wants to retrieve
        try:
            num_articles = int(message.content.split(' ')[1])
        except:
            await message.channel.send("Please enter a valid number of articles to retrieve.")
            return

        # Get the topic the user wants to retrieve articles for
        topic = ' '.join(message.content.split(' ')[2:])
        if not topic:
            topic = 'general'

        # Retrieve the news headlines
        querystring = {"apiKey": news_api_key, "country": "us", "category": topic}
        response = requests.request("GET", news_url, params=querystring)
        articles = json.loads(response.text)['articles']

        # Limit the number of articles retrieved based on the user's input
        articles = articles[:num_articles]

        # Summarize the articles and send them in a message
        for article in articles:
            summary = summarize_article(article['url'])
            await message.channel.send(f"{summary}\n{article['url']}")


bot.run(TOKEN)
