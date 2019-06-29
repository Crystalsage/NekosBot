#https://discordapp.com/oauth2/authorize?client_id=594472175478505483&scope=bot&permissions=52288

import discord, requests, asyncio, random

Client = discord.Client()
BotID = 594472175478505483
Token = open("Token.txt", 'r').read()


Categories = ['femdom', 'tickle', 'classic', 'ngif', 'erofeet', 'meow', 'erok', 'poke', 'les', 'v3', 'hololewd', 'nekoapi_v3.1', 'lewdk', 'keta', 'feetg', 'nsfw_neko_gif', 'eroyuri', 'kiss', '8ball', 'kuni', 'tits', 'pussy_jpg', 'cum_jpg', 'pussy', 'lewdkemo', 'lizard', 'slap', 'lewd', 'cum', 'cuddle', 'spank', 'smallboobs', 'goose', 'Random_hentai_gif', 'avatar', 'fox_girl', 'nsfw_avatar', 'hug', 'gecg', 'boobs', 'pat', 'feet', 'smug', 'kemonomimi', 'solog', 'holo', 'wallpaper', 'bj', 'woof', 'yuri', 'trap', 'anal', 'baka', 'blowjob', 'holoero', 'feed', 'neko', 'gasm', 'hentai', 'futanari', 'ero', 'solo', 'waifu', 'pwankg', 'eron', 'erokemo']

SendCategories = "\n".join(Categories)

def GetURL(BaseUrl):
    resp = requests.get(BaseUrl)
    URL = resp.json()["url"]

    return(URL)

@Client.event
async def on_ready(): # Connection confirmation.
    print(f"We have logged in as {Client.user}.")

@Client.event # Event wrapper.
async def on_message(message, *args):
    print(f"\nNew message in {message.channel}:") # Outputs message in the terminal.
    print(f"    Author: {message.author} / {message.author.id}\n    Screen name: {message.author.name}\n    Message: {message.content}\n    Date: {message.created_at}")


    if message.content.startswith("!nekos"):
        Option = message.content.split(" ")[1]

        if Option.lower() == "random":
            Category = random.choice(Categories)

        elif Option.lower() in Categories:
            Category = Option.lower()

        elif Option.lower() == "help":
            await message.channel.send(f"The available categories are:```{SendCategories}```")

        else:
            await message.channel.send("That is not a valid option! Use `!nekos help` for a category list.")

        try:
            BaseURL = f"https://www.nekos.life/api/v2/img/{Category}"
            URL = GetURL(BaseURL)
            await message.channel.send(URL)
        except UnboundLocalError:
            print("")
    


Client.run(Token)