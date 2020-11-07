import discord
from discord.ext import commands
from discord import File
import os


class MAT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='question', aliases=['q'])
    @commands.guild_only()
    async def question_request(self, ctx, year: int, q: str):
        if not os.path.isdir(f'papers/{year}'):
            await ctx.send("We don't have that one on file yet.")
            return
        if not os.path.isfile(f'papers/{year}/q/{q}.png'):
            await ctx.send("We don't have that file yet.")
            return

        await ctx.channel.send(f"MAT {year}, Question {q}", file=File(f'papers/{year}/q/{q}.png'))

    @question_request.error
    async def question_request_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Format your message as >q (year e.g. 02) (question, e.g 1A or 2)")
        else:
            print(error)

    @commands.command(name='solution', aliases=['s'])
    @commands.guild_only()
    async def solution_request(self, ctx, year: int, q: str):
        if not os.path.isdir(f'papers/{year}'):
            await ctx.send("We don't have that one on file yet.")
            return
        if not os.path.isfile(f'papers/{year}/s/{q}.png'):
            await ctx.send("We don't have that file yet.")
            return

        file = File(f'papers/{year}/s/{q}.png')
        file.filename = f"SPOILER_{file.filename}"

        await ctx.channel.send(f"MAT {year}, Solution to Q{q}", file=file)

    @solution_request.error
    async def solution_request_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send("Format your message as >q (year e.g. 02) (question, e.g 1A or 2)")
        else:
            print(error)


def setup(bot):
    bot.add_cog(MAT(bot))
