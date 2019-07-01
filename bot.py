#https://discordapp.com/oauth2/authorize?client_id=594472175478505483&scope=bot&permissions=52288

import discord, requests, asyncio, random, io


Client = discord.Client()
BotID = 594472175478505483
Token = open("Token.txt", 'r').read()


AllCategories = ['classic', 'les', 'hololewd', 'lewdk', 'keta', 'feetg', 'nsfw_neko_gif', 'kuni', 'tits', 'pussy_jpg', 'cum_jpg', 'pussy', 'lewdkemo', 'lewd', 'cum', 'spank', 'smallboobs', 'Random_hentai_gif', 'nsfw_avatar', 'boobs', 'solog', 'bj', 'yuri', 'trap', 'anal', 'blowjob', 'holoero', 'hentai', 'futanari', 'solo', 'pwankg', 'femdom', 'tickle', 'ngif', 'erofeet', 'meow', 'erok', 'poke', 'eroyuri', 'kiss', '8ball', 'lizard', 'slap', 'cuddle', 'goose', 'avatar', 'fox_girl', 'hug', 'gecg', 'pat', 'feet', 'smug', 'kemonomimi', 'holo', 'wallpaper', 'woof', 'baka', 'feed', 'neko', 'gasm', 'waifu', 'eron', 'erokemo']

NSFcategories = ['classic', 'les', 'hololewd', 'lewdk', 'keta', 'feetg', 'nsfw_neko_gif', 'kuni', 'tits', 'pussy_jpg', 'cum_jpg', 'pussy', 'lewdkemo', 'lewd', 'cum', 'spank', 'smallboobs', 'Random_hentai_gif', 'nsfw_avatar', 'boobs', 'solog', 'bj', 'yuri', 'trap', 'anal', 'blowjob', 'holoero', 'hentai', 'futanari', 'solo', 'pwankg']

SafeFWcategories = ['femdom', 'tickle', 'ngif', 'erofeet', 'meow', 'erok', 'poke', 'eroyuri', 'kiss', '8ball', 'lizard', 'slap', 'cuddle', 'goose', 'avatar', 'fox_girl', 'hug', 'gecg', 'pat', 'feet', 'smug', 'kemonomimi', 'holo', 'wallpaper', 'woof', 'baka', 'feed', 'neko', 'gasm', 'waifu', 'eron', 'erokemo']

class Nekos:
    def __init__(self, Choice, CategoryList):
        if Choice.lower() in CategoryList:
            self.Choice = Choice

        elif Choice.lower() == "random":
            self.Choice = random.choice(CategoryList)

    def GetURL(self):
        BaseURL = f"https://www.nekos.life/api/v2/img/{self.Choice}"
        resp = requests.get(BaseURL)
        URL = resp.json()["url"]

        return(URL)

    def ShowImage(self, url):
        GETimage = requests.get(url)
        Image = io.BytesIO(GETimage.content)
        return(Image)

@Client.event
async def on_ready():
    print(f"We have logged in as {Client.user}.")


@Client.event
async def on_message(message, *args):
    print(f"\nNew message in {message.channel} by {message.author.name} at {message.created_at}")

    if message.content.startswith("!nekos"):    
        Option = message.content.split(" ")[1]

        if message.channel.is_nsfw():
            ListType = AllCategories
        else:
            ListType = SafeFWcategories

        SendCategories = "\n".join(ListType)

        if Option.lower() == "help":
            await message.channel.send(f"The available commands are:```{SendCategories}```You can also use `!nekos random` if you can't decide.")

        elif not message.channel.is_nsfw() and Option in NSFcategories:
            await message.channel.send("You have selected a NSFW category but you're not in a NSFW channel, please enter a NSFW channel or select a SFW category.")

        else:
            Request = Nekos(Option, ListType)
            try:
                URL = Request.GetURL()
                Image = Request.ShowImage(URL)
                await message.channel.send(file=discord.File(fp=Image, filename=URL.split('/')[-1]))

            except AttributeError:
                await message.channel.send("This is not a valid category! Use `!nekos help` to view the categories.")

            

Client.run(Token)