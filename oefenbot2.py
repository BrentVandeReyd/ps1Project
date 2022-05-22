import random
import discord
from discord.ext import commands



bot = commands.Bot(command_prefix="!")


@bot.event
async def on_connect():
  print ("Bot has started!")
  await bot.change_presence(status=discord.Status.online,activity=discord.Game('Making a discordbot'))

@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server')


@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server')


#commands
@bot.command()
async def test(ctx):
  await ctx.send ("Test Back!")

@bot.command()
async def tekst(ctx):
  await ctx.send ('dit is tekst')

@bot.command()
async def hello(ctx):
  await ctx.send ("Hello How are you!")

@bot.command()
async def github(ctx):
  await ctx.send ("https://github.com/BrentVandeReyd")

@bot.command()
async def portfolioArne(ctx):
  await ctx.send ("https://arnevg.sinners.be/")

@bot.command()
async def portfolioCisse(ctx):
  await ctx.send ("https://cissem03.sinners.be/")

@bot.command()
async def portfolioSeppe(ctx):
  await ctx.send ("https://seppeve.sinners.be/")

@bot.command()
async def list(ctx):
  await ctx.send ("Dit is de lijst van al de commands")
  await ctx.send ("!github")
  await ctx.send("!portfolioArne")
  await ctx.send("!portfolioCisse")
  await ctx.send("!portfolioSeppe")
  await ctx.send("!poll")
  await ctx.send("!kick")
  await ctx.send("!ban")
  await ctx.send("!unban")
  await ctx.send("!cr")

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send (f"{member.mention} is gekicked voor het overtreden van de regels")

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send (f"{member.mention} is gebanned voor het overtreden van de regels")

@bot.command()
async def poll(ctx, *, question):
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"{question} \n✅ = Yes**\n**❎ = No")
    await message.add_reaction('✅')
    await message.add_reaction('❎')


@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


@bot.command()
async def cr(ctx):
    embed = discord.Embed(title="CoolRate", description=f"You are {random.randrange(101)}% Cool", color = discord.Color.dark_blue())
    await ctx.send(embed = embed)

#DO NOT TOUCH!

TOKEN = "OTY4MTgxMjQzOTUyOTE4NTg5.YmbHDA.IyhIOviDIOhMiupQNEIVijirZEs"

bot.run(TOKEN)