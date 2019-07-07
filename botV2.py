#https://discordapp.com/oauth2/authorize?client_id=594472175478505483&scope=bot&permissions=52288

import asyncio, discord
from discord.ext import commands
from setup import *


# Define bot
bot = commands.Bot(command_prefix=config['prefix'], case_insensitive=True)
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user.name}.")

@bot.event
async def on_disconnect():
    print(f"{bot.user.name} has disconnected.")


@bot.command(aliases=['s'])
async def show(ctx, *args):
    choice = " ".join(args)
    choice = choice.split(' ')[0]

    # Check if channel is SFW.
    if not ctx.message.channel.is_nsfw():
        if choice in SFW_categories or choice.lower() == "random":
            Request = Nekos(choice, SFW_categories)

            url = Request.get_url()
            Image = Request.show_image(url)

            return await ctx.message.channel.send(file=discord.File(fp=Image, filename=url.split('/')[-1]))

        elif choice in NSFW_categories:
            return await ctx.message.channel.send("I'm sorry, this is a NSFW category. Please enter a NSFW channel to view this category.")

        else:
            return await ctx.message.channel.send("This category does not exist.")
    

    # Channel is NSFW.
    elif ctx.message.channel.is_nsfw():
        if choice in all_categories or choice.lower() == "random":
            Request = Nekos(choice, all_categories)

            url = Request.get_url()
            Image = Request.show_image(url)

            return await ctx.message.channel.send(file=discord.File(fp=Image, filename=url.split('/')[-1]))
        
        else:
            return await ctx.message.channel.send("This category does not exist.")


@bot.command(aliases=['h'])
async def help(ctx):
    sfw = "\n    ".join(SFW_categories)
    nsfw = "\n    ".join(NSFW_categories)
    categories = f"""SFW:
    {sfw}
NSFW:
    {nsfw}"""
    await ctx.message.author.create_dm()
    await ctx.message.author.send(f"The available commands are:\n```nekos.show 'category' (alias: s)\nnekos.help (alias: h)```\nAvailable categories:```random (If you can't decide)\n{categories}```")
    await ctx.message.channel.send("Check your DM's :wink:")

bot.run(config['token'])