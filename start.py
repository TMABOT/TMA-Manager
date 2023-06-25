import sys
import sqlite3
import base64
import io
import discord
from dotenv import load_dotenv
import os
from discord.ext import commands
import requests
import asyncio
import random

#Set an admin user
AdminUser = ''
#pass if no user is set
try:
    AdminUser = str(sys.argv[1])
except:
    pass
#Check for user, if none, make user none
if AdminUser == '':
    AdminUser = 'none'
#Print debug
print(AdminUser)

#Load .env with discord token
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

#Set command prefex to !
bot = commands.Bot(command_prefix="~")

@bot.command()
async def list_banned_ips(ctx):
    if not (executor == AdminUser):
        await ctx.send("Cannot complete. Requester does not have permissions")
        print("Exiting function...")
        return 0
    con = sqlite3.connect('TMA.db')
    cur = con.cursor()
    cur.execute("SELECT username FROM users")
    await ctx.send("--------Banned Users----------")
    for row in cur.fetchall():
       await ctx.send(row[0])
       await ctx.send("------------------")

@bot.command()
async def block_ip(ctx, arg1):
    if not (executor == AdminUser):
        await ctx.send("Cannot complete. Requester does not have permissions")
        print("Exiting function...")
        return 0
    await os.system("docker exec tmbo_cont /bin/bash -c 'sudo ufw deny from "+arg1+" to any")

@bot.command()
async def list_block_ip(ctx):
    if not (executor == AdminUser):
        await ctx.send("Cannot complete. Requester does not have permissions")
        print("Exiting function...")
        return 0
    await ctx.send("--------Blocked IPs----------")
    await ctx.send(os.system("docker exec tmbo_cont /bin/bash -c 'sudo ufw status numbered"))
    await ctx.send("------------------")

@bot.command()
async def unblock_ip(ctx, arg1):
    if not (executor == AdminUser):
        await ctx.send("Cannot complete. Requester does not have permissions")
        print("Exiting function...")
        return 0
    await os.system("docker exec tmbo_cont /bin/bash -c 'sudo ufw allow from "+arg1+" to any")
#
@bot.command()
async def restart_server(ctx):
    if not (executor == AdminUser):
        await ctx.send("Cannot complete. Requester does not have permissions")
        print("Exiting function...")
        return 0
    await os.system("sudo docker exec -it tmbo_cont ash")

async def retsrat_script(ctx):
    if not (executor == AdminUser):
        await ctx.send("Cannot complete. Requester does not have permissions")
        print("Exiting function...")
        return 0
    await os.system("./start.sh")

@bot.command()
async def TMAManager_help(ctx):
    if not (executor == AdminUser):
        await ctx.send("Cannot complete. Requester does not have permissions")
        print("Exiting function...")
        return 0
    await ctx.send("block_ip: Block an IP inside of docker")
    await ctx.send("unblock_ip: Unblock an IP inside of docker")
    await ctx.send("list_block_ip: List all blocked IPs")
    await ctx.send("restart_server: Restart docker server")
    await ctx.send("retsrat_script: Go on guess")

bot.run(TOKEN)
