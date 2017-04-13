#############################################################################
#bot .py


from discord.ext import commands
#Discord Commands


import json 
#For our secrets.json


import asyncio 
#For async and asyncio stuff


with open('datafolder/secrets.json', 'r') as f:
    secrets = json.loads(f.read())              
#This is for the loading of our json file.


token = secrets['token']   
prefix = secrets['prefix']
bot = commands.Bot(command_prefix=prefix)
#This sets the variables token, prefix, and bot to there respective json 
#key.. remember {"key":"value"}


@bot.event
#This is put at the start of bot events in the main bot file
#This does not work if you add to an event in a cog though so keep that 
#in mind

async def on_ready():
#This defines what is done when bot is ready


    print('\n################')
    print("Bot is online!")
    print('################')
    print('Logged in as:')
#Basic print statements


    print(bot.user.name)
#bot.user.name is the name of the bot


    print(bot.user.id)
#this is the bot id


    print('Prefix: ', prefix)
    print('#################\n')
#More basic print statements


    #### <-- LOADING COGS --> ####
    bot.load_extension('cogs.test')
    print("COG TEST LOADED")
#This is the loading of your cogs you can choose to do this as a loop or 
#individually


bot.run(token)
#The command that runs your bot based on your token

#############################################################################
#Test cog

from discord.ext import commands
#Discord commands 


class Test:
    """TESTING COG"""

    def __init__(self, bot):
        self.bot = bot
#Starting of the cog class Test affects the last line of this file


    @commands.command(pass_context=True)
#commands.command defines this as a command
#Pass context = True basically is added when you use ctx in the next 
#line which we will go over in a second...


    async def test(self, ctx):
        """|  Testing Testing..."""
#This defines test as a command so you can do [p]test where [p] = prefix 
#and the part in """is a description for the command""" 

    
#Your code will follow that line above
        await self.bot.say("Testing is good {}".format(ctx.message.author.mention))
#The part inside .format() that says ctx.message.author.mention which 
#will mention whoever does the 'test' command.


def setup(bot):
    bot.add_cog(Test(bot))
#This is where class Test come into play this is needed at the end of 
#each cog to work.

#############################################################################
