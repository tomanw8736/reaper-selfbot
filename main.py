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
            print('[SUCCESS] Embed Sent')
            await ctx.send(embeds=[embed])

        # randomly generates a penis with length between 1-10
        @bot.command()
        async def penis(ctx):
            amount = random.randint(1, 10)
            size = '=' * amount
            content = '8' + size + 'D'
            print('[SUCCESS] Penis Sent')
            await ctx.send(content)


        # decides if someones gay (totally not rigged)
        @bot.command()
        async def aretheygay(ctx, user):
            print('[SUCCESS] Running gay test')
            #print(user)
            res = random.randint(1, 100)
            if res == 1:
                await ctx.send(user + ' is not gay!')
            else:
                await ctx.send(user + ' is gay!')

        # decides if someones trans (totally not a bitcoin miner)
        @bot.command()
        async def aretheytrans(ctx, user):
            print('[SUCCESS] Running trans test')
            res = random.randint(1, 100)
            if res == 1:
                await ctx.send(user + ' is not trans!')
            else:
                await ctx.send(user + ' is trans!')
            return
       
       # sends an embed with information on a pinged user
        @bot.command()
        async def userinfo(ctx, user=None):
            if not user:
                print('[ERROR] No user specified!')
                return
            else:
                userID = user.replace("@", "")
                userID = userID.replace("<", "")
                userID = userID.replace(">", "")
                userObject = bot.get_user(userID)
                print('[SUCCESS] Got user!')
                avatar = userObject.internal_avatar
                avatarID = avatar.id
              #  print(avatarID)
                avatarURL = "https://autumn.revolt.chat/avatars/" + avatarID + "?max_side=256"

                # send userdata
                userData = pyvolt.SendableEmbed(
                    title="Reaper Selfbot v0.1.0 | Made by: tomanw#0380",
                    description=f'''
                    Display Name: {userObject.display_name}
                    Username: {userObject.name}#{userObject.discriminator}
                    User ID: {userObject.id}
                    Online: {userObject.online}
                    Bot: {userObject.bot}
                    Avatar: {avatarURL}
                    '''
                )

                await ctx.send(embeds=[userData])
        

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
                title="Reaper SelfBot v0.1.0 | Made by: tomanw#0380",
                description='''
                ----------------------    
                --**COMMANDS**--
                ----------------------
                - .help : Shows this message

                - .penis : Sends a unicode penis of random length
                - .aretheygay [user] : Runs a gay test (totally not rigged and totally not a miner)
                - .aretheytrans [user] : Runs a trans test (totally not a bitcoin miner)

                - .userinfo [user] : Send an embed with information about the user
                ''', # lol wtf is this
            )
            print('[SUCCESS] Sent Help Embed')
            await ctx.send(embeds=[embed])
        
        # debug commands
        @bot.command()
        async def ping(ctx):
            await ctx.send(f"Response time: {round(bot.latency * 1000)}ms")
        
        bot.run(os.getenv('TOKEN'), bot=False)

rClient = Reaper('.')
rClient.run()

