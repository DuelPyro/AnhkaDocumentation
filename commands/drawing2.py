import discord

import random

from discord.ext import commands


def setup(bot):
    bot.add_command(threeplusone)

  #Command Group
@commands.group()
async def threeplusone(ctx):
  if ctx.invoked_subcommand is None:
        await ctx.send(f"That ain't a subcommand, ya goof!")

@threeplusone.group()
async def fluff (ctx):
  if ctx.invoked_subcommand is None:
        await ctx.send(f"You need to specify, ya goof! (Romance or Platonic)")


  #Sub Commands
   
   #Angst
@threeplusone.command(name="angst",
            usage="<someone><someone else>",
            description="Gives you an angsty 3 + 1 drawing prompt! (CW for manipulation + implied emotional abuse!)",
            help="")
async def angst(ctx, arg1, arg2):
    angstlist = [["saved", "they were too late."], ["loved", "they didn't."], ["helped out", "they realized it wasn't appreciated."], ["'comforted'", "their act was found out."], ["lied to", "it backfired."], ["yelled at", "the other yelled back."]]

    person1 = arg1
    person2 = arg2
    index = random.randint(0, len(angstlist)-1)
    option = angstlist[index]
    prompt = [option[0], option[1]]
    await ctx.channel.send(":pen_ballpoint: | Three times where " + person1 + " " + prompt[0] + " " + person2 + " and one time " + prompt[1])

   #Fluff (Romance)
@fluff.command(name="romance",
            usage="<someone><someone else>",
            description="Gives you a romantic fluffy 3 + 1 drawing prompt!",
            help="")
async def romance(ctx, arg1, arg2):
    fromancelist = [["made breakfast for", "they woke up to eggs and bacon."], ["hugged", "they both kissed."], ["sang a song for", "they heard the other humming the tune."], ["supported", "they relied on the other."], ["gave a hug to", "they got one back."], ["danced without", "they danced together."], ["stargazed without", "they stargazed together."], ["missed", "the other appeared while they were thinking about them."], ["got a gift for", "the other made a gift for them."]]

    person1 = arg1
    person2 = arg2
    index = random.randint(0, len(fromancelist)-1)
    option = fromancelist[index]
    prompt = [option[0], option[1]]
    await ctx.channel.send(":pen_ballpoint: | Three times where " + person1 + " " + prompt[0] + " " + person2 + " and one time " + prompt[1])


   #Fluff (Platonic)
@fluff.command(name="platonic",
            usage="<someone><someone else>",
            description="Gives you a platonic fluffy 3 + 1 drawing prompt!",
            help="")
async def platonic(ctx, arg1, arg2):
    fplatoniclist = [["recommended a game to", "the other showed them a video game they really want."], ["bought snacks for", "they received a homemade meal from the other."], ["lost a Smash match to", "they finally won."], ["said 'aren't you tired of being nice' to", "the other finally went apeshit."], ["spoke about their desire to sightsee to", "the other drove them out around town."], ["picked up and threw", "the other hurled them into a trash can."], ["pranked", "got pranked back."]]

    person1 = arg1
    person2 = arg2
    index = random.randint(0, len(fplatoniclist)-1)
    option = fplatoniclist[index]
    prompt = [option[0], option[1]]
    await ctx.channel.send(":pen_ballpoint: | Three times where " + person1 + " " + prompt[0] + " " + person2 + " and one time " + prompt[1])
   