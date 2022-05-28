from email import message
from re import M
import discord
import asyncio
from discord.ext import commands
import time
import mysql.connector
import random
import json
import logging

#log naar een file
logging.basicConfig(
        filename='example.log',
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
logging.debug('')
logging.info('')
logging.warning('')


prefix = "!keldevs."
bot = commands.Bot(command_prefix=prefix)









messaged = []
@bot.event
async def on_ready():
    logging.info("Alles is klaar om te goan!")





@bot.event
async def on_message(message):
    global messaged

    if message.content.lower() == "!keldevs.jm":
        await message.channel.send("Je moeder!")
        logging.info("!keldevs.jm uitgevoerd door {}".format(message.author))


    elif message.content.lower() == "!keldevs.pingtest":
        if message.author.guild_permissions.administrator:
            await pingtest(message)
            logging.info("Allowed pingtest voor {}".format(message.author))
        else:
             await message.channel.send("Je hebt niet de nodige rechten om dit command uit te voeren. Sorry pik!")
             logging.warning("Denied pingtest van {}".format(message.author))    


    elif message.content.lower() == "!keldevs.helpmij":
        await helpmij(message)
        logging.info("!keldevs.helpmij uitgevoerd door {}".format(message.author))


    elif message.content.lower() == "!keldevs.sysops":
        if message.author.guild_permissions.administrator:
            await sysops(message)
            logging.info("Allowed sysops door {}".format(message.author))
        else:
             await message.channel.send("Je hebt niet de nodige rechten om dit command uit te voeren. Sorry pik!")
             logging.info("denied sysops van {}".format(message.author))    

    elif message.content.startswith("!keldevs.purge "):
        if message.author.guild_permissions.administrator:
          limit_amount = int(message.content.split("!keldevs.purge ")[1])
          await message.channel.purge(limit = limit_amount)
          logging.info("Allowed purge door {}".format(message.author)) 
        else:
             await message.channel.send("Je hebt niet de nodige rechten om dit command uit te voeren. Sorry pik!")
             logging.info("denied purge van {}".format(message.author))                

    elif message.content.startswith("!keldevs.wiebenik"):
        if message.author.guild_permissions.administrator:
            await message.channel.send("Je bent admin")
            logging.info("!keldevs.wiebenik uitgevoerd door {}".format(message.author))
        else:
             await message.channel.send("Je hebt niet de nodige rechten om dit command uit te voeren. Sorry pik!")
             logging.war("denied purge van {}".format(message.author))                





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



















bot.run('')  # Dit is de bot token!
