from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Hello! Study bot is ready!')
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Hello! Study bot is ready!')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def add(ctx, x, y):
    result = int(x) + int(y)
    await ctx.send(f"{x} + {y} = {result}")

@bot.command()
async def subtract(ctx, x, y):
    result = int(x) - int(y)
    await ctx.send(f"{x} - {y} = {result}")

@bot.command()
async def multiply(ctx, x, y):
    result = int(x) * int(y)
    await ctx.send(f"{x} * {y} = {result}")


@bot.command()
async def divide(ctx, x, y):
    result = int(x) / int(y)
    await ctx.send(f"{x} / {y} = {result}")

bot.run(BOT_TOKEN)