"""Dank farm made by pluton

auto beg + fish + dig + hunt + macro detect tricking
"""
from discord.ext import commands
from colorama import init, Fore
import asyncio
import random
import os
import sys
import dotenv


TOKEN = dotenv.dotenv_values(".env")["token"]
prefix = dotenv.dotenv_values(".env")["prefix"]
client = commands.Bot(command_prefix=prefix,self_bot=True)
init(convert=True)

@client.event
async def on_ready():
    os.system("cls")
    os.system("title Dank farmer - Pluton#5551")
    intro = f"""{Fore.GREEN}
______            _     ______                   
|  _  \          | |    |  ___|                  
| | | |__ _ _ __ | | __ | |_ __ _ _ __ _ __ ___  
| | | / _` | '_ \| |/ / |  _/ _` | '__| '_ ` _ \ 
| |/ / (_| | | | |   <  | || (_| | |  | | | | | |
|___/ \__,_|_| |_|_|\_\ \_| \__,_|_|  |_| |_| |_|

{Fore.RED}Prefix:{Fore.CYAN} {prefix}
{Fore.RED}Farmer:{Fore.CYAN} {client.user}
{Fore.RESET}"""
    print(intro) 


@client.command(name="farmtime", aliases=["dankfarm","start","itsfarmtime","farm"])
async def farmer(ctx):
    global count, toggle
    await ctx.message.delete()
    
    count = 0
    toggle = True
    
    while toggle:
        try:
            count += 1
            await ctx.channel.send("pls beg")
            await asyncio.sleep(round(random.random(),2)) #  seems more legit
            await ctx.channel.send("pls hunt")
            await asyncio.sleep(round(random.random(),2))
            await ctx.channel.send("pls dig")
            await asyncio.sleep(round(random.random(),2))
            await ctx.channel.send("pls fish")
            print(f"\r[{Fore.GREEN}+{Fore.RESET}] Farm {Fore.CYAN}#{count}{Fore.RESET} sent.",end="")
        except Exception as e:
            print(f"\r[{Fore.RED}!{Fore.RESET}] Error! {e}")
            sys.exit()
        await asyncio.sleep(random.randint(45,50)) #  random number between 45, 50. 

@client.command(name="stop")
async def stop(ctx):
    global toggle
    await ctx.message.delete()
    toggle = False
    print(f"\r[{Fore.RED}!{Fore.RESET}] Farm stopped as {Fore.GREEN}#{count}{Fore.RESET}!",end="")
@client.command(name="kill")
async def kill(ctx):
    await ctx.message.delete()
    client.close()
    


client.run(TOKEN,bot = False)