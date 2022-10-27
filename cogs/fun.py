# bibliotecas
from helpers.texts import eightball
from discord.ext import commands
from discord import app_commands
from helpers.assets import embed
from uwuipy import uwuipy
import discord
import random


# realiza a criação da classe cog
class Fun(commands.Cog):
    def __init(self, yume: commands.AutoShardedBot):
        self.yume = yume

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun is Ready!!')

    # Fortune Cookie
    @app_commands.command(name='fortune', description='Let me check your fortune with cookies!')
    async def fortune(self, interaction: discord.Interaction):

        cookie = discord.File('./media/cookie.gif', filename='cookie.gif')
        lines = open('./helpers/fortunes.txt').read().splitlines()
        fortune = random.choice(lines)

        embed.set_author(name=fortune, icon_url=interaction.user.avatar.url)
        embed.set_image(url='attachment://cookie.gif')
        embed.set_footer(text="This is what the cookie said to Yume!")
        await interaction.response.send_message(embed=embed, file=cookie)

    # Uwuify
    @app_commands.command(name='uwuify', description='it makes you s-s-speak w-wike (˘ε˘) t-t-t-this?!?!')
    async def uwuify(self, interaction: discord.Interaction, *, phrase: str):

        uwu = uwuipy(None, 0.3, 0.3, 0.2, 1)
        await interaction.response.send_message(uwu.uwuify(phrase))

    # 8ball
    @app_commands.command(name='8ball', description='let the 8 ball gives you a answer!')
    async def eightball(self, interaction: discord.Interaction, *, question: str):

        answer = random.choice(eightball())
        await interaction.response.send_message(answer)


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Fun(yume))