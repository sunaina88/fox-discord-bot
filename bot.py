import discord
import os
import sys
import asyncio
import requests
import json


def get_fox():
    """sends a random image of a fox"""
    response=requests.get('https://randomfox.ca/floof/')
    json_data=json.loads(response.text)
    return json_data['image']


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        print('🦊 Commands: $hello, $fox')
        await self.change_presence(activity=discord.Game(name="$fox for fox images!"))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello {message.author.mention} !')

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


# Get the token from the environment
TOKEN = os.getenv('DISCORD_TOKEN')
if not TOKEN:
    print("❌ ERROR: DISCORD_TOKEN not set!")
    sys.exit(1)


# Run the bot
async def main():
    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)

    try:
        await client.start(TOKEN)
    except KeyboardInterrupt:
        await client.close()
    except Exception as e:
        print(f"Bot crashed: {e}")
        await asyncio.sleep(5)
        await main()

    if __name__ == "__main__":
        asyncio.run(main())
