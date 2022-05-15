# This looks horrible
lyrics = [
    "nevergonna",
    "nevergonnagiveyouup",
    "nevergonnaletyoudown",
    "nevergonnarunaround", 
    "anddesertyou",
    "nevergonnamakeyoucry",
    "nevergonnasaygoodbye",
    "nevergonnatellalie",
    "andhurtyou",
    "nevergon",
    "giveuup"
]

chars = [' ', '`', '~', '!', '@', '#', '$', '%', '^', 
            '&', '*', '(', ')', '-', '_', '+', '=',
            '[', ']', '{', '}', ':', ';', '|', '\\',
            ',', '.', '<', '>', '/', '?']

def check_lyrics(message):
    # process the string
    for char in chars:
        if char in message:
            message = message.replace(char, '')

    if len(message) == 1:
        return True
    
    for line in lyrics:
        if line in message.lower():
            return True
    
    return False