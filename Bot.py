import discord
import json
import os
import requests
import urllib

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

who_count = 0


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('hi') or message.content.lower().startswith('hello'):
        await message.channel.send('Hi!')
        return

    if message.content.startswith('Who') | message.content.startswith('who'):
        global who_count
        who_count += 1
        if who_count > 1:
            await message.channel.send('stop annoying me')
        else:
            await message.channel.send('what?')
        return

    if message.content.startswith('bye') | message.content.startswith('goodbye'):
        await message.channel.send('yaaaaaaaay')
        return

    if message.content.startswith('tell me a joke please'):
        headers = {'User-Agent': 'annoying-discord-bot/0.0.1', 'Accept': 'application/json'}
        r = requests.get('https://icanhazdadjoke.com/', headers=headers)
        response = json.loads(r.text)
        await message.channel.send(response["joke"])
        return

    if message.content.startswith('tell me a joke') | message.content.startswith('Tell me a joke'):
        await message.channel.send('whats the magic word')
        return

    if message.content.startswith('gif'):
        query = message.content.split(" ", 1)
        data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=" + query + "&api_key=YOUR_API_KEY&limit=5").read())
        print(json.dumps(data, sort_keys=True, indent=4))

    await message.add_reaction('\U0001f44d')


client.run(os.environ.get("DISCORDKEY"))
