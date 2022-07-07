#Drawing Prompts
  
import discord 

import random

from discord.ext import commands



def setup(bot):
    bot.add_command(draw)

  #Command Group
@commands.group()
async def draw(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f"That ain't a subcommand, ya goof!")

  #Lists
romancelist = ["Coffee Shop", "Romantic Date", "Early Morning Hugs", "Game Night", "Pillow Fort", "Late Night Movie", "There's Only One Bed", "There's Only One Bed (But Also A Couch Downstairs)", "First Date"]
colorlist = ["blue", "red", "green", "purple", "white", "black", "cyan", "orange", "yellow"]
fightlist = ["With Tanks", "Hand-To-Hand", "With Food", "Over Food", "Playfully", "A Bloody Battle", "In A Video Game", "With Swords", "Side By Side", "Through An Apocalypse", "Rebellion Soldiers Get Caught", "For Your Life", "Against A Former Ally", "Against Former Allies"]
horrorlist = ["Haunted House", "Vengeful Ghost", "Murder At A Mansion", "The Group Got Split", "Foggy Woods At Night", "Something's In The House...", "Weird Noise Upstairs", "Murderer On TV Then Suddenly The Lights Go Out", "Shadow Outside The Door"]
duolist = [" protects ", " saves ", " bothers ", " throws ", " draws ", " brushes ", " fires ", " kicks ", " kicks (playful) ", " fights ", " makes food for ", " stops ", " gives a flower to ", " dabs on ", " plays Smash with ", " fights alongside ", " downloads a car with ", " travels with ", " fights with ", " betrays ", " sings for ", " pokes ", " insults ", " stares at ", " surprises ", " defends ", " blows a kiss to ", " backflips over ", " scares ", " makes food with ", " puts makeup on ", " puts hairclips on ", " puts bows on ", " braids the hair of "]

  #Sub Commands

    #Romance
@draw.command(name="romance",
            usage="<romance>",
            description="Gives you a romantic drawing prompt!",
            help="")
async def romance(ctx, *args):
    index = random.randint(0, len(romancelist)-1)
    prompt = romancelist[index]
    await ctx.channel.send(":pencil2: | Your romance prompt is " + prompt + "!") 

  

    #Colors
@draw.command(name="color",
            usage="<color>",
            description="Challenges you to only use the shade of the given color in a drawing!",
            help="")
async def color(ctx, *args):
    index = random.randint(0, len(colorlist)-1)
    prompt = colorlist[index]
    await ctx.channel.send(":pencil2: | Only use shades of the color " + prompt + "!") 

    #Fight
@draw.command(name="fight",
            usage="<fight>",
            description="Gives you a fighting action drawing prompt!",
            help="")
async def fight(ctx, *args):
    index = random.randint(0, len(fightlist)-1)
    prompt = fightlist[index]
    await ctx.channel.send(":pencil2: | Your fight prompt is " + prompt + "!") 

    #Horror
@draw.command(name="horror",
            usage="<horror>",
            description="Gives you a horror drawing prompt!",
            help="")
async def horror(ctx, *args):
    index = random.randint(0, len(horrorlist)-1)
    prompt = horrorlist[index]
    await ctx.channel.send(":pencil2: | Your horror prompt is " + prompt + "!") 

 #Three Sentence Prompts
@draw.command(name="duo",
            usage="<someone><someone else>",
            description="Gives you a short prompt with two people!",
            help="")
async def angst(ctx, arg1, arg2):
    person1 = arg1
    person2 = arg2
    index = random.randint(0, len(duolist)-1)
    prompt = duolist[index]
    await ctx.channel.send(":bulb: | " + person1 + prompt + person2 + "!") 

 