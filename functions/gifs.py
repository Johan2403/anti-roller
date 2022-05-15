from discord.ext import commands
from antiroller import gif_detect as gd

class Gifs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if "gif" or ".gif" in message.content and "http" in message.content:
            if gd.check_gifs(message.content):
                await message.delete()

        