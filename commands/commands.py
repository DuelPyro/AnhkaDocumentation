import discord 
import asyncio
import random

from discord.ext import commands


def setup(bot):
    bot.add_command(cake)
    bot.add_command(love)
    bot.add_command(addition)
    bot.add_command(selfdoxx)
    bot.add_command(wait)
    bot.add_command(coinflip)
    
#Slice
@commands.command(
             name="slice",
             usage="", 
             description="Anhka gives you cake", 
             help="", 
             hidden=True)
async def cake(ctx):
    await ctx.send(":cake:")

#Love You
@commands.command(
             name="loveyouanhka",
             usage="", 
             description="Show Anhka your love and appreciation!", 
             help="", 
             hidden=True,
             aliases=["love"])
async def love(ctx):
    await ctx.send("Love you, " + ctx.author.name + "!")


#Addition
@commands.command(
             name="addition",
             usage="<number> <other number>",
             description="Adds two numbers",
             help="",
             hidden=False)
async def addition(ctx, arg1, arg2):
    arg1 = int(arg1)
    arg2 = int(arg2)
    ans = arg1 + arg2
    ans = str(ans)
    await ctx.send("The answer is " + ans + "!")

#Doxx
@commands.command(
             name="selfdoxx",
             usage="",
             description="Grabs your IP Address (Totally!)",
             help="",
             hidden=False)
async def selfdoxx(ctx):
    await ctx.send(":man_dancing:")
    await asyncio.sleep(1)
    await ctx.send(":dancer:")
    await asyncio.sleep(1)
    await ctx.send(":man_dancing:")
    await asyncio.sleep(1)
    await ctx.send("120.75.127.154")

#Nyake
@commands.command(
             name="nuke",
             usage="", 
             description="BOOM! BOOM! BOOM!", 
             help="", 
             hidden=True)
async def cake(ctx):
    await ctx.send("TACTICAL NYA-KE INCOMING!")
    await asyncio.sleep(1)
    await ctx.send("3")
    await asyncio.sleep(1)
    await ctx.send("2") 
    await asyncio.sleep(1)
    await ctx.send("1") 
    await asyncio.sleep(1)
    await ctx.send(":boom:")

#Wait
@commands.command(
             name="wait",
             usage="[amount of seconds]", 
             description="It's like a timer!", 
             help="", 
             hidden=False)
async def wait(ctx, arg1):
     try:
        time = int(arg1)
        await asyncio.sleep(time)
        await ctx.send("Time!")
     except ValueError:
        await ctx.send("Use an actual number :hand_splayed: :rolling_eyes:")
        return

#Coinflip
@commands.command(
             name="coinflip",
             usage="", 
             description="Original command do not steal", 
             help="", 
             hidden=False)
async def coinflip(ctx):
    flip = random.randint(0, 1)
    if flip == 1:
        await ctx.send("Heads!")
    else:
        await ctx.send("Tails!")
   
