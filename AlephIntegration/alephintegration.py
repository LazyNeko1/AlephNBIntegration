import aiohttp, asyncio, nbapi
import nbutil_ao as nb

from discord.ext import commands

class NekoBotInt():
    class info():
        def __init__(self):
            self.nekobot_fullname = "Neko-Bot-Cheliese"
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


class BOT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
