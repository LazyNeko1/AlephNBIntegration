#Discord Bot Integration hosted by NekoBot

import aiohttp, asyncio, nbapi
import nbutil_ao as nb

from discord.ext import commands
#Variable Assignment for UTILS module under NekoBotInt()



class NekoBotInt():
    nekobot_fullname = nb.NekoBot.Fullname
    nekobot_age = "11"
    class info():
        def __init__(self):
            self.nekobot_fullname = "Neko-Bot-Chliese"
            self.nekobot_age = "11"
    class post():
        def __init__(self, url, headers, typeOf):
            """

            :param url: URL to get info from
            :param headers: Headers for URL
            :param typeOf: Type of GET (Quests, Stats, etc.)
            """

            self.HTTP = nb.HTTP(url = url, headers = headers)

        def STATS(self, UUID = 0, stat_3string = None, stat_1line = None):
            pass
    class get():
        def __init__(self, url, headers, typeOf):
            """

            :param url: URL to get info from
            :param headers: Headers for URL
            :param typeOf: Type of GET (Quests, Stats, etc.)
            """
            self.needs=typeOf
        def STATS(self, UUID = 0):
            nb.HTTP.get()


class BOT_out(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
