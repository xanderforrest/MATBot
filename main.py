import discord
from discord.ext import commands
from secrets import token


def get_prefix(bot, message):
    prefixes = ['>']

    if not message.guild:
        return '>'

    return commands.when_mentioned_or(*prefixes)(bot, message)


initial_extensions = ['cogs.mat']

bot = commands.Bot(command_prefix=get_prefix, description='MAT Bot')

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Successfully logged in and booted...!')


bot.run(token, bot=True, reconnect=True)