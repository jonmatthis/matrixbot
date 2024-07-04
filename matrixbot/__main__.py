import simplematrixbotlib as botlib

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

creds = botlib.Creds("https://matrix.org", os.getenv('USERNAME'), os.getenv('PW'))

print(creds)
bot = botlib.Bot(creds)
print(bot)
PREFIX = '!'
@bot.listener.on_message_event
async def echo(room, message):
    """
    Example command that "echoes" arguements.
    Usage:
    example_user- !echo say something
    echo_bot- say something
    """
    match = botlib.MessageMatch(room, message, bot, PREFIX)
    if match.is_not_from_this_bot() and match.prefix() and match.command("echo"):
        await bot.api.send_text_message(room.room_id, " ".join(arg for arg in match.args()))

print("running bot..")
bot.run()
print("done!")
