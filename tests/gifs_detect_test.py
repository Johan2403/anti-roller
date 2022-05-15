from antiroller import gif_detect as gd

lyrics = gd.hashes


gifs = [
    "https://tenor.com/view/rickroll-roblox-rick-roll-nevergonnagiveyouup-bobux-gif-18123245"
]

dup_gif_links = [
    "https://cdn.discordapp.com/attachments/975006123646144542/975032929359110274/notatall.gif",
    "https://cdn.discordapp.com/attachments/975006123646144542/975040777644294195/bruh.gif"
]

def test_check_gifs_default():
    for link in gifs:
        assert gd.check_gifs(link)

def test_duplicate_gifs():
    for link in dup_gif_links:
        assert gd.check_gifs(link)