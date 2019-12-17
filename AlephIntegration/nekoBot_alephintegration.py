# Discord Bot Integration hosted by NekoBot

import aiohttp
import asyncio
import nbapi
from discord.ext import commands

import nbutil_ao as nb


# Variable Assignment for UTILS module under NekoBotInt()
class toNb:
    stringOut_Quest1 = None

    def __init__(self):
        pass


class NekoBotInt:
    nekobot_fullname = nb.NekoBot.Fullname
    nekobot_age = nb.NekoBot.age
    BASEURL = nb.aleph.BaseUrl

    class info:
        def __init__(self):
            self.nekobot_fullname = "Neko-Bot-Chliese"
            self.nekobot_age = "11"

    class post:
        def __init__(self, url, headers=None, typeOf=None):
            """
            :param url: URL to get info from
            :param headers: Headers for URL
            :param typeOf: Type of GET (Quests, Stats, etc.)
            """

            self.HTTP = nb.HTTP(url=url, headers=headers, typeOf=typeOf)

        def STATS(self, UUID=0, stat_3string=None, stat_1line=None):
            pass

    class get:
        def __init__(self, url, headers=None, typeOf=None):
            """
            :param url: URL to get info from
            :param headers: Headers for URL
            :param typeOf: Type of GET (Quests, Stats, etc.) (None due to it not being used in this specific GET request. That's used by the UTIL lib.)
            """
            self.needs = typeOf
            self.headers = headers
            self.url = url

        def STATS(self, UUID=0):
            nb.HTTP(url=self.url, headers=self.headers).get(UUID=UUID).UserStats_FROMID()


class BOT_out(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def quests(self, ctx):
        command = ctx.message.content.split(" ", 1)[1]
        if command.startswith("view"):
            print("ViewQuest FROMUTILS")

            toNb.stringOut_Quest1 = {"QuestOutputToBot": True}
