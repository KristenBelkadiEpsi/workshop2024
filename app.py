import discord
from discord.ext import commands
import os
import dotenv
from detoxify import Detoxify
import pandas as pd

model = Detoxify("multilingual")
toxicity_limit = 0.6


dotenv.load_dotenv()
# Intention d'authentification (requis avec les nouvelles versions de discord.py)
intents = discord.Intents.default()
intents.message_content = True  # Permet au bot de lire le contenu des messages
bot = commands.Bot(command_prefix="!", intents=intents)

def is_toxic(text):
     predict = model.predict([text])
     data_frame = pd.DataFrame(predict).round(5)
     return bool(data_frame["toxicity"][0] >= toxicity_limit)

@bot.event
async def on_ready():
    print(f'Le bot est connecté en tant que {bot.user}')


@bot.event
async def on_message(message:discord.Message):
    if message.author != bot.user:
        if is_toxic(message.content):
            await message.author.send("Votre message à été suprimé car jugé toxique")
            await message.delete()

@bot.command()
async def repete(ctx, *, message: str):
    await ctx.send(message)

#Environnement Variable TOKEN
token = os.environ.get("TOKEN")
bot.run(token)