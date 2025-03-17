from pyvolt.ext import commands
import pyvolt
import asyncio
import os
import base64
from dotenv import load_dotenv
import random
import wikipedia

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

       # sends an embed with information on a pinged user
        @bot.command()
        async def userinfo(ctx, user : pyvolt.User):
            if not user:
                print('[ERROR] No user specified!')
                return
            else:
                print('[SUCCESS] Got user!')
                try:
                    avatar = user.internal_avatar
                    avatarID = avatar.id
                    #  print(avatarID)
                    avatarURL = "https://autumn.revolt.chat/avatars/" + avatarID + "?max_side=256"
                except:
                    avatarURL = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmemepedia.ru%2Fwp-content%2Fuploads%2F2023%2F08%2Fbojkisser-768x512.jpg&f=1&nofb=1&ipt=7637bafe9a3d022d032b8dc31e02635c8bc2c6a2a34af6c9626276182195e2f3&ipo=images"


                # send userdata
                userData = pyvolt.SendableEmbed(
                    title="Reaper Selfbot v0.1.0 | Made by: tomanw#0380",
                    description=f'''
                    Display Name: {user.display_name}
                    Username: {user.name}#{user.discriminator}
                    User ID: {user.id}
                    Online: {user.online}
                    Bot: {user.bot}
                    [Avatar]({avatarURL})
                    ''',
                )

                await ctx.send(embeds=[userData])
                return

        # base64 encoding and decoding
        @bot.command()
        async def b64(ctx, mode = 'encode', string: str = 'ENTER SOMETHING'):
            try:
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
            except:
                print('[ERROR] Encountered an error while executing command!')


        # wikipedia command(s)
        # syntax: .wiki [search/summary/link] [query/page name]
        @bot.command()
        async def wiki(ctx, mode = 'search', string: str = 'Test'):
            if mode == 'search':
                try:
                    result = wikipedia.search(string) # getting possible pages
                    formatResult = ", ".join(result) # seperating them by , in a string
                    await ctx.send("Results: " + formatResult) # sending the results
                except:
                    await ctx.send('[ERROR] I honestly dont know what error caused this')
            elif mode == 'summary':
                try:
                    result = wikipedia.summary(string) # getting a summary
                    formatResult = result.replace('\n', "\n>") # replacing new lines with new lines with quote blocks
                    if len(formatResult) >= 2000: # if the summary exceeds the character limit for revolt
                        print('Too long! Splitting string!')
                        PartOne, PartTwo = formatResult[:len(formatResult)//2], formatResult[len(formatResult)//2:] # splits the summary into two strings
                        await ctx.send(f'Summary [1/2]:\n>{PartOne}')
                        await ctx.send(f'Summary [2/2]:\n>{PartTwo}')
                    else: # if the summary does NOT exceed the character limit
                        await ctx.send(f'Summary:\n>{formatResult}')
                    
                except: # if the user doesn't put in a valid page name/other error
                    await ctx.send("Please input a valid page name!")
            elif mode == 'link':
                try:
                    result = wikipedia.page(string) # gets the page object
                    await ctx.send(f'Page URL: <{result.url}>') # sends the page URL/link
                except:
                    await ctx.send('[ERROR] Once again, no clue what caused this one')
        
        @bot.command()
        async def vale(ctx, query):
            await ctx.send(f'<https://vale.rocks/search?q={query}>')
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

                - .userinfo [user] : Send an embed with information about the user
                - .b64 [encode/decode] [string] : Encodes/Decodes a string to base64
                - .wiki [search/summary/link] [query] : Uses the wikipedia library to get pages information from Wikipedia
                - .vale [query] : Returns a link to vale's epic search with your query

                -----------------------------
                --**JOIN MY SERVER**--
                -----------------------------
                [Join Friendly Now!](https://rvlt.gg/jjd9Ddt4)
                ''', # lol wtf is this
            )
            print('[SUCCESS] Sent Help Embed')
            await ctx.send(embeds=[embed])
        
        # debug commands
        
        # sends a test embed
        @bot.command()
        async def embedTest(ctx):
            embed = pyvolt.SendableEmbed(
                title="Title",
                description="Description"
            )
            print('[SUCCESS] Embed Sent')
            await ctx.send(embeds=[embed])
        
        bot.run(os.getenv('TOKEN'), bot=False)

rClient = Reaper('.')
rClient.run()

