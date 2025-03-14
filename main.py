from pyvolt.ext import commands
import pyvolt
import asyncio
import os
from dotenv import load_dotenv
import random

TITLE = '''
╔════════════════════════════════════════════════════╗
║  ██████╗ ███████╗ █████╗ ██████╗ ███████╗██████╗   ║
║  ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗  ║
║  ██████╔╝█████╗  ███████║██████╔╝█████╗  ██████╔╝  ║
║  ██╔══██╗██╔══╝  ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗  ║
║  ██║  ██║███████╗██║  ██║██║     ███████╗██║  ██║  ║
║  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝  ║
╚════════════════════════════════════════════════════╝                                               

'''

# utilities
load_dotenv()

class Reaper:
    def __init__(self, prefix):
        self.prefix = prefix
    
    def run(self):
        print(TITLE)
        bot = commands.Bot(command_prefix=self.prefix, self_bot=True)

        @bot.command()
        async def embedTest(ctx):
            embed = pyvolt.SendableEmbed(
                title="Title",
                description="Description"
            )
            await ctx.send(embeds=[embed])

        # randomly generates a penis with length between 1-10
        @bot.command()
        async def penis(ctx):
            amount = random.randint(1, 10)
            size = '=' * amount
            content = '8' + size + 'D'
            await ctx.send(content)
        

#        DO NOT UNCOMMENT - I AM NOT AT FAULT
#        IF YOU GET BANNED FOR USING THIS FEATURE
#        @bot.command()
#        async def spam(ctx, count, message):
#            for i in range(int(count)):
#                await ctx.send(message)


        # HELP COMMAND
        @bot.command()
        async def help(ctx):
            embed = pyvolt.SendableEmbed(
                title="Reaper SelfBot v0.1.0",
                description='''
                    
                ║ **COMMANDS** ║
                ╚══════════╝
                - .help : Shows this message
                ''', # lol wtf is this
            )
            await ctx.send(embeds=[embed])

        
        bot.run(os.getenv('TOKEN'), bot=False)

rClient = Reaper('.')
rClient.run()

