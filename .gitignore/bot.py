import discord
from discord.ext import commands
import time
import asyncio
import datetime as DT
import os



heros = ("orbotp/.gitignore/heros")
client = discord.Client()

access_token = os.environ["TOKEN"]

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity=discord.Game(" pour me decouvrir :help"))
    print("je suis pret")
   


@client.event
async def on_message(message):
    id = client.get_guild( 414142903649173534 )
    v_u = ["zoordax#7914", "KyNeK974#0692"]
    v2_u = ["toigal#5408","zoordax#7914", "KyNeK974#0692"]
    toig = ["Nananette Anne#6943", "zoordax#7914", "toigal#5408"]
    channels = ["👽-monstres-👽", "test", "🌐-site-web-🌐"]
    user = ["test"]
    kyn = ["🎤-no-micro-mix-🎤", "🤡-humour-🤡","🎧 dialogue ORB (Main) 🎧"]
    youtube = "https://www.youtube.com/channel/UCWQH8J7AY0AwWqIIdDFbLTQ"
    site = "https://lords-mobile.info/"
    ping_ = client.latency
    ping = round(ping_ * 1000 )
     
   


            
    if str(message.channel) in user and str(message.author) in v_u:
        if message.content.find ("$hello") != -1:
            await message.channel.send ("hi")
        elif message.content == "$users":
            await message.channel.send (f"""# of Members: {id.member_count}, at {DT.datetime.now()}""")
            
    
    if str( message.channel ):
        if message.content == ":help":
            embed = discord.Embed( title="orbot" , description="salut ! je suis orbot !", color = 0xff1c21 )
            embed.add_field( name="Monstres" , value="je peux te donner les differentes composition pour les monstres pour cela direction <#548863999362596865>" )
            embed.add_field ( name = "site web", value=" tu as aussi plusieur façon d'avoir divers info sur le jeu pour cela je te laisse aller  dans le channel <#591345643587502090>  pour taper !orb")
            await message.channel.send( content=None , embed=embed, delete_after = 300 )
            await asyncio.sleep(1)
            await message.delete()
            

    if str( message.channel ) in channels :
        if message.content == "!monstres":
            embed = discord.Embed( title="**Monstre**" , description="Pour utiliser le bot taper : \n **!le_monstre**\nsi vous voulez un exemple pour utiliser le bot taper : \n!exemple"  , color = 0xff1c21 )
            embed.add_field( name="***>>>***Tous les monstres***<<<***" , value="\n ailedegivre \nailenoires\nbetedesneiges\nchaman\ndrider\nepinator\ngargantua\ngolem\ngriffon\nfaucheuse\nmorphalange\ntroyen\nlarve\nnoceros\nreineabeille\nsabrecroc\ntitan\nwyrm" )
            await message.channel.send( content=None , embed=embed , delete_after = 60 )
            await asyncio.sleep(60)
            await message.delete()
            
            
    if str( message.channel ) :
        if message.content == "!orb":
            file = discord.File("heros/orb.jpg", filename="orb.jpg")
            embed = discord.Embed( title="ORB" , description="***Ici les different moyens de trouver orb***", color = 0xff1c21 )
            embed.add_field( name="***>>><:yt:591246747800567830>YOUTUBE<:yt:591246747800567830><<<***" , value= youtube )
            embed.add_field( name="***>>><:site:591301400416485376> SITE ORB<:site:591301400416485376><<<***" , value= site )     
            await message.channel.send( file=file , embed=embed, delete_after = 300 )
            await asyncio.sleep(1)
            await message.delete()

            
            
    if str(message.channel) :
        if message.content == "!ping" :
            embed = discord.Embed( title = ":pong: PONG! :pong:",  color = 0xff1c21)
            embed.add_field(name = "***super-vitesse***", value = f"<:sablier:596030953374220319>mon temps de latence est de {ping} ms")
            await message.channel.send(content = None , embed=embed)
                                     
            
            
            
    if str( message.channel ) in channels:
        if message.content.find ("!exemple") != -1:
            await message.channel.send("!drider", delete_after = 3600)
            await asyncio.sleep(60)
            await message.delete()
    


    if str( message.channel ) in channels and str(message.author) in v_u:
        if message.content.find ("!loutre") != -1:
            await message.channel.send(" koya est out !!!", delete_after=3)
            await asyncio.sleep(3)
            await message.delete()
            
            
    if str( message.channel ) in kyn and str(message.author) in toig :
        if message.content.find ("!toigal2") != -1:
            await message.channel.send(file=discord.File('heros/toigal2.jpg'), delete_after = 600)
            await asyncio.sleep(600)
            await message.delete()  
            
    if str( message.channel ) in kyn and str(message.author) in toig :
        if message.content.find ("!toigal") != -1:
            await message.channel.send(file=discord.File('heros/toigou.gif'), delete_after = 600)  
            await asyncio.sleep(600)
            await message.delete()    
            
            

    if str( message.channel ) in channels :
        if message.content.find ("!golem") != -1:
            await message.channel.send(file=discord.File('heros/golem.jpg'), delete_after = 600)
            await asyncio.sleep(600)
            await message.delete()            

    if str( message.channel ) in kyn and str(message.author) in v2_u :
        if message.content.find ("!panda") != -1:
            await message.channel.send(file=discord.File('heros/panda.jpg'), delete_after = 600)
            await asyncio.sleep(600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!wyrm") != -1:
            await message.channel.send(file=discord.File('heros/wyrm.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels:
        if message.content.find( "!titan" ) != -1:
            await message.channel.send( file=discord.File( 'heros/titan.jpg' ), delete_after = 3600) 
            await asyncio.sleep(3600)
            await message.delete()


    if str( message.channel ) in channels :
        if message.content.find ("!sabrecroc") != -1:
            await message.channel.send(file=discord.File('heros/sabrecroc.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!reineabeille") != -1:
            await message.channel.send(file=discord.File('heros/abeille.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!noceros") != -1:
            await message.channel.send(file=discord.File('heros/noceros.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()


    if str( message.channel ) in channels :
        if message.content.find ("!larve") != -1:
            await message.channel.send(file=discord.File('heros/larve.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()


    if str( message.channel ) in channels :
        if message.content.find ("!troyen") != -1:
            await message.channel.send(file=discord.File('heros/troyen.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()



    if str( message.channel ) in channels :
        if message.content.find ("!morphalange") != -1:
            await message.channel.send(file=discord.File('heros/morphalange.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()



    if str( message.channel ) in channels :
        if message.content.find ("!betedesneiges") != -1:
            await message.channel.send(file=discord.File('heros/Bneige.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!faucheuse") != -1:
            await message.channel.send(file=discord.File('heros/faucheuse.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!griffon") != -1:
            await message.channel.send(file=discord.File('heros/griffon.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!gargantua") != -1:
            await message.channel.send(file=discord.File('heros/gargantua.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!epinator") != -1:
            await message.channel.send(file=discord.File('heros/epinator.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()


    if str( message.channel ) in channels :
        if message.content.find ("!drider") != -1:
            await message.channel.send(file=discord.File('heros/drider.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!ailedegivre") != -1:
            await message.channel.send(file=discord.File('heros/givre.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!ailenoire") != -1:
            await message.channel.send(file=discord.File('heros/Anoir.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()

    if str( message.channel ) in channels :
        if message.content.find ("!chaman") != -1:
            await message.channel.send(file=discord.File('heros/chaman.jpg'), delete_after = 3600)
            await asyncio.sleep(3600)
            await message.delete()


client.run(access_token)
 


