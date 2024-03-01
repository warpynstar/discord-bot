from discord.ext import commands
import discord

BOT_TOKEN = 'MTIxMzA0MDIyMjEyOTA5NDY3Ng.G0cb3O.24gVH5fdwrlJsKvFWLjR1KEZ_ZikmIZ5FFM3Rs'
CHANNEL_ID = 1213044260295807028

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

bot.run(BOT_TOKEN)