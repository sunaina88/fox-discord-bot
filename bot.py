import discord
import os
import sys
import requests
import json
from dotenv import load_dotenv 
from keepalive import keep_alive


keep_alive()
load_dotenv()
# Get the token from the environment
TOKEN = os.getenv('DISCORD_TOKEN')
if not TOKEN:
    print("ERROR!")
    sys.exit(1)


def get_fox():
    """sends a random image of a fox"""
    response=requests.get('https://randomfox.ca/floof/')
    json_data=json.loads(response.text)
    return json_data['image']


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print('🦊 Commands: $hello, $fox')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello friend !')

        elif message.content.startswith('$fox'):
            try:
                fox_url = get_fox()
                embed = discord.Embed(
                    title="🦊 Here is your Random Fox!",
                    color=discord.Color.orange()
                )
                embed.set_image(url=fox_url)
                await message.channel.send(embed=embed)
            except Exception as e:
                await message.channel.send(f"Error: {str(e)}")


# Run the bot
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
