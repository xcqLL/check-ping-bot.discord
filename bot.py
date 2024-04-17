import discord
from discord.ext import commands

# Set up intents 
intents = discord.Intents.all()
intents.messages = True 

# Create a Bot instance with command prefix "/" and defined intents (YOU CAN CUSTOM PREFIX)
bot = commands.Bot(command_prefix="/", intents=intents)

# Event handler for when the bot successfully connects to Discord
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Define a command named "myping" to check bot's latency
@bot.command()
async def myping(ctx):
    # Calculate bot's latency to the Discord server
    latency = round(bot.latency * 1000)  

    # Create an embed message displaying the latency
    embed = discord.Embed(
        title="Your Ping :",
        description=f"{latency} ms",
        color=0x1400fd  
    )

    # Send the embed message back to the channel where the command was invoked
    await ctx.send(embed=embed)

bot.run("YOUR_TOKEN")
