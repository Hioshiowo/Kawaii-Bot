import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from discord import Member
import second

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_encouragment(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

@client.event
async def on_message(message):
  if message.author.bot:
    return
  if "$config" in message.content:
    await message.channel.send("**Configs are not Released.. yet...**\r\n"
                               "Configs for Clients")
  if "$help" in message.content:
    await message.channel.send("**help page for Kawaii-Bot**\r\n"
                               "$about        $config       $inspire\r\n"
                               "$release      $github       $uwu\r\n"
                               "more in the Future!")

  if message.content.startswith("!userinfo"):
    args = message.content.split(" ")
    if len(args) == 2:
        member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
        if member:
          embed = discord.Embed(title="User info! {}".format(member.name),
          description="User info of".format(member.mention),
          color=0x22a7f0)
          embed.add_field(name="Join date", value=member.joined_at.strftime("%d/%m/%Y, %H:%M:%S"), inline=True)

          embed.add_field(name="Discord Join date", value=member.created_at.strftime("%d/%m/%Y, %H:%M:%S"), inline=True)
          rollen = ""
          for role in member.roles:
            if not role.is_default():
              rollen += "{} \r\n".format(role.mention)
          if rollen:
            embed.add_field(name="roles", value=rollen, inline=True)
          embed.set_thumbnail(url=member.avatar_url)
          embed.set_footer(text="Kawaii-bot ©TM®")
          await message.channel.send(embed=embed)
  if "!lov3" in message.content:
    await message.channel.send("**I luv you Anni C: <3**")
  if "EARTHHACK 3.0" in message.content:
    await message.channel.send("**Gamesense GitHub!:**\r\n"
                                  "https://github.com/Gopro366")
    r = requests.get('https://github.com/')
    print(r.status_code)
            
  if "-cosmos.jar" in message.content:
    await message.channel.send("**Cosmos GitHub!:**\r\n"
                                "https://github.com/linustouchtips/cosmos")  
  if "-rape" in message.content:
    await message.channel.send("@everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone @everyone")
  
  if "-release date" in message.content:
    await message.channel.send("**Kawaii Client Release Soon**\r\n"
                                "#info! for the Info you fag!")
  
  if "sad" in message.content:
    await message.channel.send("don't be sad.\r\n"
                              "Be happy https://tenor.com/view/dog-smile-happy-good-boy-dog-smile-happy-good-boy-gif-21703225")
    r = requests.get('https://google.com/')
    print(r.status_code)
  if "!setup" in message.content:
    from discord_webhook import DiscordWebhook, DiscordEmbed

    content = 'This is a Basic Command List what the Bot offers to you!'

    webhook = DiscordWebhook(url='https://ptb.discord.com/api/webhooks/921940877344145408/_2krGoTSiAk3ay7fzqJ6VwpiofyELoxZ4mZX3S1gAQlZHV3FwabJvd1L5DApEMQcfxIW')

    embed = DiscordEmbed(title='Kawaii-Bot is Currently in Beta', color=242424)
    embed.set_author(name='Kawaii international Cheats-', url='https://www.nautiljon.com/images/perso/00/97/tohsaka_rin_11979.jpg', icon_url='https://www.nautiljon.com/images/perso/00/97/tohsaka_rin_11979.jpg')
    embed.set_footer(text='Kawaii-bot International')
    embed.set_timestamp()
    embed.add_embed_field(name='Cheats release Date', value='Current cheats are free, but we are recommending EARTHHACK 3.0 because of the Many settings and the Good performance')
    embed.set_image(url='https://www.nautiljon.com/images/perso/00/97/tohsaka_rin_11979.jpg')
    webhook.add_embed(embed)
    respose = webhook.execute()
  

  if "Zoomy" in message.content:
    await message.channel.send("Zoomy is a Sussy Nigger!\r\n"
                              "Everyone hits headshots exept for him")
  


keep_alive()
client.run("ODkyNzkzNTE5MzQ4MDE1MjA1.YVSEwg.-C2c4Z3RC3WGqW4jYsGi45mmxPo")
