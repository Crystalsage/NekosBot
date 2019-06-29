#https://discordapp.com/oauth2/authorize?client_id=594472175478505483&scope=bot&permissions=52288

import discord, requests, asyncio, random


Client = discord.Client()
BotID = 594472175478505483
Token = open("Token.txt", 'r').read()


Categories = ['femdom', 'tickle', 'classic', 'ngif', 'erofeet', 'meow', 'erok', 'poke', 'les', 'v3', 'hololewd', 'nekoapi_v3.1', 'lewdk', 'keta', 'feetg', 'nsfw_neko_gif', 'eroyuri', 'kiss', '8ball', 'kuni', 'tits', 'pussy_jpg', 'cum_jpg', 'pussy', 'lewdkemo', 'lizard', 'slap', 'lewd', 'cum', 'cuddle', 'spank', 'smallboobs', 'goose', 'Random_hentai_gif', 'avatar', 'fox_girl', 'nsfw_avatar', 'hug', 'gecg', 'boobs', 'pat', 'feet', 'smug', 'kemonomimi', 'solog', 'holo', 'wallpaper', 'bj', 'woof', 'yuri', 'trap', 'anal', 'baka', 'blowjob', 'holoero', 'feed', 'neko', 'gasm', 'hentai', 'futanari', 'ero', 'solo', 'waifu', 'pwankg', 'eron', 'erokemo']
SendCategories = "\n".join(Categories)


class Nekos:
    def __init__(self, Choice):
        if Choice.lower() in Categories:
            self.Choice = Choice

        elif Choice.lower() == "random":
            self.Choice = random.choice(Categories)

    def GetURL(self):
        try:
            BaseURL = f"https://www.nekos.life/api/v2/img/{self.Choice}"
            resp = requests.get(BaseURL)
            URL = resp.json()["url"]

        except AttributeError:
            URL = "This is not a valid category! Use `!nekos help` to view the categories."

        return(URL)


@Client.event
async def on_ready():
    print(f"We have logged in as {Client.user}.")


@Client.event
async def on_message(message, *args):
    print(f"\nNew message in {message.channel}:")
    print(f"    Author: {message.author} / {message.author.id}\n    Screen name: {message.author.name}\n    Message: {message.content}\n    Date: {message.created_at}")


    if message.content.startswith("!nekos"):
        Option = message.content.split(" ")[1]

        if Option.lower() == "help":
            await message.channel.send(f"The available commands are:```{SendCategories}```You can also use `!nekos random` if you can't decide.")

        else:
            Request = Nekos(Option)
            URL = Request.GetURL()

            await message.channel.send(URL)
    

Client.run(Token)