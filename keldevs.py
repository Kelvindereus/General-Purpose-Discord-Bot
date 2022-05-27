import discord
import asyncio
from discord.ext import commands
import time
prefix = "!keldevs."
bot = commands.Bot(command_prefix=prefix)
channel = bot.get_channel("979410173665878016")


@bot.event
async def on_ready():
    print("Alles is klaar om te goan!")

@bot.command()
async def helpmij(ctx):
    embedVar = discord.Embed(title="KelDevs Commands!", description="I'm a pretty little hot Discord bot, written and hosted by Kelvin!", color=0x00ff00)
    embedVar.add_field(name="Commando scherm", value="!keldevs.help", inline=True)             
    embedVar.add_field(name="Jemoeder joke", value="!keldevs.jemoeder", inline=True)
    embedVar.add_field(name="Admin-Delete messages", value="!keldevs.purge", inline=True)        
    embedVar.add_field(name="Admin-Announce", value="!keldevs.announce", inline=True)          
    embedVar.add_field(name="Zie bot message latency", value="!keldevs.ping", inline=True)             
    embedVar.add_field(name="Zie bot database latency", value="!keldevs.dbping", inline=True) 
    await ctx.send(embed=embedVar)

@bot.command()
async def jemoeder(ctx):
    latency = bot.latency 
    await ctx.send("Je moeder")

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! {0}'.format(round(bot.latency, 1)))

@bot.command()
async def dbping(ctx):
    latency = bot.latency 
    await ctx.send(latency)

@bot.command()
async def announce(ctx, channel: discord.TextChannel, arg1):
    embed=discord.Embed(title="Aankondiging", description="{}".format(arg1), color=0xFF5733)
    await channel.send(embed=embed)

@bot.command()
@commands.has_role('「🕶」ServerDeveloper (Admin)')
async def BotSysOps(ctx):
    embedVar = discord.Embed(title="KelDevs SysOps info!!", description="I'm a pretty little hot Discord bot, written and hosted by Kelvin!", color=0x00ff00)
    embedVar.add_field(name="IP", value="10.0.0.22", inline=True)             
    embedVar.add_field(name="VMID", value="108", inline=True)
    embedVar.add_field(name="BotPAD", value="/home/bot/keldevs.py", inline=True)          
    await ctx.send(embed=embedVar)

@bot.command(name="purge")
@commands.has_role('「👑」Oprichter, 「👑」Administrator, Moderator')
async def clean(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.send("Er zijn {} verwijderd".format(int), delete_after=5)
        
@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Je mag dat niet doen")




















bot.run('')  # Where 'TOKEN' is your bot token

  
