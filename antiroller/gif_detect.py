import hashlib
from urllib.request import urlopen, Request

keywords = [
    "rickroll",
    "nevergonnagiveyouup"
]

# TODO: Find a way to serialize the hashes
hashes = [
    "f8893f144a854bc411653a273cc4a2e1"
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

    for keyword in keywords:
        if keyword in link:
            hashes.append(gif_hash)
            return True

    for hash in hashes:
        if hash == gif_hash:
            return True

    return False