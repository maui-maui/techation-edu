#############################################################################
#bot .py

from discord.ext import commands
import json
import asyncio

with open('datafolder/secrets.json', 'r') as f:
    secrets = json.loads(f.read())

token = secrets['token']
prefix = secrets['prefix']
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print('\n################')
    print("Bot is online!")
    print('################')
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('Prefix: ', prefix)
    print('#################\n')

    #### <-- LOADING COGS --> ####
    bot.load_extension('cogs.test')
    print("COG TEST LOADED")

bot.run(token)

#############################################################################
#Test cog

from discord.ext import commands


class Test:
    """TESTING COG"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def test(self, ctx):
        """|  Testing Testing..."""
    
        #Your code will go here
        await self.bot.say("Testing is good {}"
.format(ctx.message.author.mention))

def setup(bot):
    bot.add_cog(Test(bot))

#############################################################################
