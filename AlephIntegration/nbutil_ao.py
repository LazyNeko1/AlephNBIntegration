# Basic UTILS file for the Aleph Integration. Modified version of NBUTILs (pypi)

import os
import aiohttp

# Main File
import nekoBot_alephintegration as main


class aleph:
    BaseUrl = "http://aleph.neko-bot.net"
    quest1 = main.toNb.stringOut_Quest1

    def __init__(self):
        self.GetAddress = None
        self.quest1 = aleph.quest1
        self.firstname = NekoBot.Fname # Default name (when asked)
        self.lastname = NekoBot.Lname # DO NOT USE WHEN TALKING, only for any sort of dialog box.
        self.fullname = NekoBot.Fullname # please for the love of god don't use this one hehe
    def NPCoutput(self,context,playername="Neko",extras=None):
        context=context.lower()
        if context.startswith("Helllo"):pass


class NekoBot:
    Fname = "Neko"
    Mname = "Bot"
    Lname = "Chliese"
    Fullname = f"{Fname} {Mname} {Lname}"
    age = 11

    def __init__(self):
        self.Fullname = NekoBot.Fullname


class HTTP:
    osNam = os.name
    osSys = os.system

    def __init__(self, headers, url, timeFrame=0):
        """
        :param url: URL to get from
        :param headers: Headers for URL
        :param timeFrame: Time between HTTP requests (depreciated)
        """
        self.headers = headers
        self.url = url
        self.timeframe = timeFrame

    def headers(self):
        return self.headers

    def URL(self):
        return self.url

    def timeFrame(self):
        """
        Mostly a useless thing, meant for time between next HTTP request (dep.)
        """
        pass

    class get:
        def __init__(self, UUID=0, UNAME=None, QUID=0):
            """
            :param UUID: User ID
            :param UNAME: UserName
            :param QUID: Quest ID
            """
            self.UUID = UUID
            self.UNAME = UNAME
            self.QUID = QUID

        def UserStats_FROMID(self):
            if self.UUID is 0 or None:
                return f"Could not get User Info from ID {self.UUID}"
            if self.UUID is not 0 or None:
                OUT = None
                return OUT

        def UserStats_FROMNAME(self):
            pass

        def QuestStats_FROMNAME(self):
            pass

        def QuestStats_FROMID(self):
            if self.QUID is not 0 or None:
                out = {"output": "ReturnValuesFromHttp", "returnId": self.QUID}
                return out
