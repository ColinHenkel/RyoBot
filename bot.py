import discord
import os
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# command prefix
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

# on_ready event
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'Failed to sync commands: {e}')

# ping command
@bot.tree.command(name="ping", description="Returns the bot's latency")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f'Pong! 🏓 {latency}ms')

# echo command
@bot.tree.command(name="echo", description="Repeats the provided message")
async def echo(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(message)

# help command
@bot.tree.command(name="help", description="Shows a list of available commands")
async def help_command(interaction: discord.Interaction):
    commands_list = [f'`/{command.name}` - {command.description}' for command in bot.tree.get_commands()]
    help_message = "\n".join(commands_list) if commands_list else "No commands available."
    await interaction.response.send_message(help_message)

# run bot
bot.run(os.getenv('TOKEN'))
