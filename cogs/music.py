# bibliotecas
from discord.ext import commands


# inicializa o cog
class Music(commands.Cog):
    def __init__(self, saturn):
        self.saturn = saturn

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Music is Ready!')

    # not yet
    @commands.command()
    async def musicy(self, ctx):
        await ctx.send(f'ainda não está pronto :c')


# registra a classe no cogs
def setup(saturn):
    saturn.add_cog(Music(saturn))