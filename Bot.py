import discord
from discord.ext import commands

prefix = "+"                                   # préfixe pour appeler le bot
bot = commands.Bot(command_prefix= prefix, description = "je sème la terrreur chez les fauteur des troubles")

# sur discord entre ** pour gras et entre * pour en italique
@bot.event
async def on_ready():
    print("ready !")

@bot.command()
async def coucou(ctx):
    await ctx.send("Coucou !")

@bot.command()
async def bonjour(ctx):
    await ctx.send("Salut *jeune padawan* tu vas bien ?")

@bot.command()
async def say(ctx, nb_repet, *text):
    nb_repet = int(nb_repet)
    for i in range(nb_repet):
        await ctx.send(" ".join(text))

@bot.command()
async def chinese(ctx, *text):
    chineseChar = "丹书匚刀巳下呂廾工丿片乚爪冂口尸Q尺丂丁凵V山乂Y乙"
    chinesetxt = []
    for word in text :
        for char  in word :
            if char.isalpha():
                index = ord(char) - ord("a")
                transform = chineseChar[index]
                chinesetxt.append(transform)
            else :
                chinesetxt.append(char)
        chinesetxt.append(" ")
    await ctx.send("".join(chinesetxt))

@bot.command()
async def serverinfo(ctx):
    serveur = ctx.guild
    serveur_name = serveur.name
    nboftxtchannels = len(serveur.text_channels)
    nbofvoicechannels = len(serveur.voice_channels)
    descript_serveur = serveur.description
    nbofpersonns = serveur.member_count
    message = f"Le Serveur **{serveur_name}** contient {nbofpersonns} personnes. \n La description du serveur est {descript_serveur}. \n Ce serveur possède {nboftxtchannels} salons textuels et {nbofvoicechannels} salons vocaux"
    await  ctx.send(message)

@bot.command()
async def getinfo(ctx, info):
    server = ctx.guild
    if info == "member_count" :
        await ctx.send(server.member_count)
    elif info == "numberofchannel" :
        await ctx.send(f"nombre de channels vocaux :{len(server.voice_channels)} \n nombre de channel textuels :{len(server.text_channels)}")
    elif info == "name" :
        await ctx.send(server.name)
    else :
        await ctx.send("je ne connais pas cette commande")


@bot.command()
async def clear(ctx, nombre : int):
    messages = await ctx.channel.history(limit = nombre + 1).flatten()
    for message in messages :
        await message.delete()

'''
@bot.command()
async def kick(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(f"{user} a été kick")
'''

'''
#            no test
@bot.command()
async def ban(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    await ctx.send(f"{user} a été ban pour {reason}.")
'''

'''
@bot.command()
async def unban(ctx, user, *reason):
    reason = " ".join(reason)
    username, userid = user.split("#")
    banneduser = await ctx.guild.bans()
    for i in banneduser :
        if i.user.name == username and i.user.discriminator == userid :
            await ctx.guild.unban(i.user, reason = reason)
            await ctx.send(f"{user} a été unban pour {reason}.")
            return
    await ctx.send(f"error {user} n'a pas été trouvé")
'''

token = "OTE4OTY4MDA1OTQ0MzAzNjI3.YbO9pg.0ZltEVRbDE1Qvx4reWOHDZIrf1E"
bot.run(token)
