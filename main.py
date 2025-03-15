from pyvolt.ext import commands
import pyvolt
import asyncio
import os
import base64
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
        async def userinfo(ctx, user : pyvolt.User):
            if not user:
                print('[ERROR] No user specified!')
                return
            else:
                print('[SUCCESS] Got user!')
                avatar = user.internal_avatar
                avatarID = avatar.id
              #  print(avatarID)
                avatarURL = "https://autumn.revolt.chat/avatars/" + avatarID + "?max_side=256"

                # send userdata
                userData = pyvolt.SendableEmbed(
                    title="Reaper Selfbot v0.1.0 | Made by: tomanw#0380",
                    description=f'''
                    Display Name: {user.display_name}
                    Username: {user.name}#{user.discriminator}
                    User ID: {user.id}
                    Online: {user.online}
                    Bot: {user.bot}
                    ''',
                    icon_url = avatarURL
                )

                await ctx.send(embeds=[userData])
        @bot.command()
        async def b64(ctx, mode = 'encode', string: str = 'ENTER SOMETHING'):
            if mode == 'encode':
                string_bytes = string.encode("ascii")
                b64_bytes = base64.b64encode(string_bytes)
                b64_string = b64_bytes.decode("ascii")
                await ctx.send(b64_string)
                return
            elif mode == 'decode':
                b64_bytes = string.encode("ascii")
                string_bytes = base64.b64decode(b64_bytes)
                decoded_string = string_bytes.decode("ascii")
                await ctx.send(decoded_string)
                return

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

