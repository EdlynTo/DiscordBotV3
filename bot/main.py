import discord
import os
#import pynacl
#import dnspython
import server
from discord.ext import commands

# bot = commands.Bot(command_prefix="$")
# TOKEN = os.getenv("DISCORD_TOKEN")

# server.server()
# bot.run(TOKEN)

import random
import pyjokes
from keep_alive import keep_alive

my_secret = os.environ['Token']
client = discord.Client()

negative_words = [
    "sad", "depressed", "unhappy", "angry", "mad", "stressed", "impossible",
    "upset","annoyed","hate"
]

encouragements = [
    "Hang in there, don't give UP!",
    "Believe in yourself and anything is possible <3",
    "Courage is going from failure to failure without losing enthusiam -Winston Churchill",
    "NEVER GIVE UP!!!!!!!!! You CAN do it! :D"
    "This is tough but you're TOUGHER!! :muscle:"
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game('$help | No violence signals for the past few days!')


#@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  msg = msg.lower()

  if msg.startswith('~attack'): #~attack reaction
      await message.channel.send(
          ":angry: HEY be nice xoxo! :broken_heart: The next time you think of attacking someone please think it over again. :smiling_face_with_3_hearts:"
      )

  if msg.startswith('~shoot'): #~shoot reaction
      await message.channel.send(
          ":angry: HEY be nice xoxo! :broken_heart: The next time you think of shooting someone please think it over again. :smiling_face_with_3_hearts: "
      )

  if msg.startswith('pls rob'): #pls rob reaction
      await message.channel.send(":angry: HEY be nice xoxo! :broken_heart: The next time you think of robbing someone please think it over again. :smiling_face_with_3_hearts:")

  if msg.startswith('c!donatesave'): #c!donatesave reward
      await message.channel.send(
          ":heart_eyes: Wow tysm for donating a save to Cousins!! :heart: As a reward you get enternal love from Counting Bot!! <3"
      )

  if any(word in msg for word in negative_words): #negative words to encouragements
      await   message.channel.send(random.choice(encouragements))
  
  
  if msg.startswith('$help'): #$help command
    await message.channel.send('''**Thank you for using Love Bot <3!!**
    This awesome bot is all about spreading LOVE! :gift_heart: :revolving_hearts: :heartpulse:
    It sends a *custom message* when someone types `.shoot`, `.attack` or `pls rob` :no_entry_sign:
    It reminds them to be **kind**!!:sparkling_heart:
    When someone is feeling __negative__, :worried:
    it reminds them that at least they're better than Christopher! /j :grin:
    Love Bot isn't that mean. :heart_eyes:
  
    **Commands:** 
    `$help` - Sends a helpful message about the bot
    `$joke` - Send a hilarious joke.
    `$loverate` - Check how much love your spreading!! The higher the percentage the more love your spreading!! <3
                               
  
    We will add more features/commands soon!! :heart_eyes: :smiling_face_with_3_hearts:''')
                      
  if msg.startswith('$joke'): #$joke command
    url = "https://dad-jokes.p.rapidapi.com/random/joke"
    headers = {
        'x-rapidapi-key': "e9adf17bc8mshbb1ffd310032e03p10d575jsn9800c9b14139",
        'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers)
    jokeMessastr(response.text['setup'])
  await msg.channel.send(jokeMessage)            

  if msg.startswith('$loverate'): #$loverate command
      loverate = (random.randrange(60, 99))
      if loverate < 75:
        await message.channel.send(f"Hmmmm... Try to spread more love. Your loverate is {loverate}%. You're not using all your love :/")
      elif loverate < 90:
        await message.channel.send(f"Wow, you're sharing quite a bit of love today!! Your loverate is {loverate}%. Congrats!")
      else:
        await message.channel.send(f"**THATS INSANE!!!** You're sharing __SOOO__ much love today!! <3 <3 Your loverate is {loverate}%.")

keep_alive() #keep alive function
client.run(os.getenv('Token'))