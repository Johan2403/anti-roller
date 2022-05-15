import hashlib
from os import getenv
from urllib.request import urlopen, Request

DEBUG_MODE = False

if getenv("DEBUG") == "TRUE":
    DEBUG_MODE = True

keywords = [
    "rickroll",
    "nevergonnagiveyouup"
]

# TODO: Find a way to serialize the hashes
hashes = [
    "f8893f144a854bc411653a273cc4a2e1",
    "ab750c1ec098e16e69a73c22dd54dae1"
]

def check_gifs(link):
    req = Request(
        link,
        data=None,
        headers= {
            'User-Agent': 'Anti Roller'
        }
    )

    file = urlopen(req)
    gif_hash = hashlib.md5(file.read()).hexdigest()

    if DEBUG_MODE:
        print("[DEBUG]: GIF Hash is", gif_hash)

    for keyword in keywords:
        if keyword in link:
            if gif_hash not in hashes:
                hashes.append(gif_hash)
            if DEBUG_MODE:
                print("[DEBUG]: hashes =", hashes)
            return True

    for hash in hashes:
        if hash == gif_hash:
            return True

    return False