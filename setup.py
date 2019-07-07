import json, os, random, requests, io

# Get config file.
current_dir = os.path.dirname(__file__)
with open(os.path.join(current_dir, 'config.json')) as config_file:  
    config = json.load(config_file)

#Get category file.
with open(os.path.join(current_dir, 'categories.json')) as category_file:  
    categories = json.load(category_file)
    SFW_categories = []
    NSFW_categories = []

    for key in categories:
        if categories[key] == "SFW":
            SFW_categories.append(key)
        elif categories[key] == "NSFW":
            NSFW_categories.append(key)
    
    all_categories = SFW_categories + NSFW_categories


class Nekos:
    def __init__(self, choice, categories):
        if choice.lower() == "random":
            self.choice = random.choice(categories)

        else:
            self.choice = choice

    def get_url(self):
        base_url = f"https://www.nekos.life/api/v2/img/{self.choice}"
        resp = requests.get(base_url)
        url = resp.json()["url"]

        return(url)

    def show_image(self, url):
        GETimage = requests.get(url)
        Image = io.BytesIO(GETimage.content)
        return(Image)