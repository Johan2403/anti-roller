try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from discord.ext import commands
from os import getenv

from functions.lyrics import Lyrics
from functions.gifs import Gifs

bot = commands.Bot("!", None, "The Rickroll protector")
BOT_TOKEN = getenv('TOKEN')
DEBUG_MODE = False

if BOT_TOKEN == None:
    print("Please set the TOKEN environment variable.")
    exit(1)

if getenv('DEBUG').lower() == "true":
    DEBUG_MODE = True

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print()

    if DEBUG_MODE:
        print("Bot running in DEBUG MODE! Sensitive info will be logged to console.")
        print("Use this only in developement environments!")
        print(f"TOKEN: {BOT_TOKEN}")
    else:
        print("Bot running in PRODUCTION MODE. Sensitive info will be hidden.")

bot.add_cog(Lyrics(bot))
bot.add_cog(Gifs(bot))

bot.run(BOT_TOKEN)