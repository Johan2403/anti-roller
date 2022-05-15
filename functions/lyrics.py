from discord.ext import commands
from antiroller import lyrics_detect as ld

class Lyrics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if "gif" not in message.content:
            if ld.check_lyrics(message.content):
                await message.delete()
        