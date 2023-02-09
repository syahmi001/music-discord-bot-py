# Main file, bot.py
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Loading config values
import os 
import config

# Loading ENV value, specifically the bot token
# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')

# If you want to use config value, comment top section and uncomment bottom one
TOKEN = config.TOKEN

# Loading bot's intent
intents = discord.Intents.default()
intents = discord.Intents().all()

commands_list: list = ["commands.music.youtube"]

bot = commands.Bot(intents=intents, command_prefix=config.Prefix)

@bot.event
async def on_ready():
    print('{0.user} Bot is ready!'.format(bot))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(config.BotStatus))
    for command in commands_list:
        try:
            print(f"Loading command {command}")
            await bot.load_extension(command)
            print(f"Loaded command {command}")
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load command {}\n{}".format(command, exc))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

bot.run(TOKEN)