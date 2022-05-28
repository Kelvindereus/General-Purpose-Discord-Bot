from email import message
from re import M
import discord
import asyncio
from discord.ext import commands
import time
import mysql.connector

prefix = "!keldevs."
bot = commands.Bot(command_prefix=prefix)

messaged = []
@bot.event
async def on_ready():
        print("Alles is klaar om te goan!")




@bot.event
async def on_message(message):
    global messaged

    if message.content.lower() == "!keldevs.jm":
        await message.channel.send("Je moeder!")

    elif message.content.lower() == "!keldevs.pingtest":
        await pingtest(message)

    elif message.content.lower() == "!keldevs.helpmij":
        await helpmij(message)

    elif message.content.lower() == "!keldevs.sysops":
        await sysops(message)

    elif message.content.lower() == "ad.purge":
            if message.author.guild_permissions.administrator:
                p = 0
                p = int(message.content.split(" ")[1])
                if (p != 0):
                    purge(limit, m)
                else:
                    await message.channel.send("Flapdrol, ik moet wel weten hoeveel berichten ik moet verwijderen")
            else:
                await message.channel.send("Sorry, deze functie is niet toegankelijk voor het plebs... uh ik bedoel mensen zonder administrator permissies")

    elif message.content.lower() == "!keldevs.birtdayin":
        await birthday(message)
   

async def pingtest(message):
    before = time.monotonic()
    message = await message.channel.send("Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong!  `{int(ping)}ms`")

async def helpmij(message):
        embedVar = discord.Embed(title="KelDevs Commands!", description="I'm a pretty little hot Discord bot, written and hosted by Kelvin!", color=0x00ff00)
        embedVar.add_field(name="Commando scherm", value="!keldevs.help", inline=True)             
        embedVar.add_field(name="Jemoeder joke", value="!keldevs.jemoeder", inline=True)
        embedVar.add_field(name="Admin-Delete messages", value="!keldevs.purge", inline=True)        
        embedVar.add_field(name="Admin-Announce", value="!keldevs.announce", inline=True)          
        embedVar.add_field(name="Zie bot message latency", value="!keldevs.ping", inline=True)             
        embedVar.add_field(name="Zie bot database latency", value="!keldevs.dbping", inline=True) 
        message = await message.channel.send(embed=embedVar)


async def sysops(message):
        embedVar = discord.Embed(title="KelDevs SysInfo!", description="I'm a pretty little hot Discord bot, written and hosted by Kelvin!", color=0x00ff00)
        embedVar.add_field(name="IP", value="10.0.0.22", inline=True)             
        embedVar.add_field(name="VMID", value="108", inline=True)
        message = await message.channel.send(embed=embedVar)

async def purge(limit, message):
    global guild
    await message.channel.purge(limit=l)
    s = await message.channel.send("purged by " + message.author.name)
    sleep(5000)
    await message.delete()
    await s.delete()

async def birtdayin(message):
    


















bot.run('DETOKEN')  # Dit is de bot token!



  
