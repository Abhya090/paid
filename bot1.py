import discord
from discord.ext import commands
import requests

# Define intents
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

# Discord bot setup with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Replace these placeholders with your actual tokens and IDs
DISCORD_BOT_TOKEN = 'MTIzMzM5Nzg5Nzg5MzQ5NTI1OTE4N.GWoG5c.ptl4UVSqijaT2fK1idbDfG-ZHLsnYsAJLXfXpg'
GITHUB_TOKEN = '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'
CODESPACE_ID = 'b35927d5-b00e-416a-b8e6-4b6430d59e13'

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')  # Ensure the string is properly terminated with quotation marks

@bot.command()
async def bgmi(ctx, *, command: str):
    """
    Command to execute a command in a Codespace in GitHub
    Usage: !bgmi <command>
    """
    # Send request to GitHub API to execute command in Codespace
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'command': f'./bgmi {command}'
    }
    response = requests.post(f'https://api.github.com/codespaces/{CODESPACE_ID}/commands', json=data, headers=headers)
    
    if response.status_code == 201:
        await ctx.send(f'Command "{command}" sent for execution in Codespace')
    else:
        await ctx.send(f'Error sending command: {response.text}')

# Run the bot
bot.run(DISCORD_BOT_TOKEN)
