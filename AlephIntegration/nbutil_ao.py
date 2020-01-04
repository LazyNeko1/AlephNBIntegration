# Basic UTILS file for the Aleph Integration. Modified version of NBUTILs (pypi)
import os

from random import randint
import aiohttp
import memories as memories
# Main File
import nekoBot_alephintegration as base

class temp:
    feelings_level_max = 10
    pass

class aleph:
    BaseUrl = "http://aleph.neko-bot.net"

    def __init__(self):
        self.GetAddress = None
        try:
            self.firstname = NekoBot.Fname  # Default name (when asked)
            self.lastname = NekoBot.Lname  # DO NOT USE WHEN TALKING, only for any sort of dialog box.
            self.fullname = NekoBot.Fullname  # please for the love of god don't use this one heh
        except NameError:
            self.firstname = None
            self.lastname = None
            self.fullname = None

    def SoulOutput(self, context=None, usage=False, ):
        if context is None and usage is None:  # Idle talk
            feelingsbase = memories.soul.feelings.output
            feelings1 = feelingsbase["1"]
            feelings2 = feelingsbase["2"]

            rh_tofeelings = randint(feelings1, feelings2)
            # calculated in memories module

            return None  # sounds.hum(rh_tofeelings)
    def feelings(self, context, extras = memories.soul.feelings.output):
        if extras["2"] < 4:
            temp.feelings_level_max = extras["2"]
    def NPCoutput(self, context, playername="Neko", extras=None):

        args = extras.lower()
        context = context.lower()
        if memories.soul.feelings.output["2"] < 4:
            hl = temp.feelings_level_max

        if context.startswith("Hello"):
            if playername is "Neko":
                return "Wait... You have the same name as me?"
            if playername is "LazyNeko":
                return "Hello, How are you doing?"
            elif playername is not "LazyNeko" or "Neko":
                return "Hello, how can I help you?"


class NekoBot:
    nekosoul = memories.soul
    Fname = "Neko"  # First Name
    Mname = "Bot"  # Middle Name
    Lname = "Chliese"  # Last Name
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
        HTTP.url = url
        HTTP.headers = headers

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
            # Likely won't happen as unique IDs for the quests are needed - otherwise I will
            # get the stats using the QuestStats_FROMID and do a search-through using a customized sorting
            # system, getting the ID using that.
            # EG:
            # "QN" : "QUID"
            # or
            # "FirstQuest" : "ID1" (yes the ID1) will be the format. Mostly to reduce any data manipulation
            # if the occasion comes around and that happens.
            # I also feel random IDs would mess things up, as having to update more things would slow
            # more things down. For example, having to update the IDs live in-game, on website,
            # and in bot would be very hard. Thats why doing it in iterations using the ID(num) prefix would help, as
            # that is what NekoBot normally does for the NBAPI module. (used to, at least)
            pass

        async def QuestStats_FROMID(self):
            if not str(self.QUID).startswith("ID"):
                self.QUID = f"ID{self.QUID}"
            if self.QUID is not "ID0" or None:
                async with aiohttp.ClientSession as nbhttp:
                    obj = await nbhttp.get(url=f"{aleph.BaseUrl}/quests/{self.QUID}/stats")
                    # NEED TO ADD THIS URL
                    # TO SITE VERY SOON
                    httpval = obj.content
                out = {"output": f"{httpval}", "returnId": self.QUID}
                return out
            if self.QUID is "ID0" or None:
                if self.QUID is not "ID0":
                    out = {"output": "Invalid ID supplied.", "returnId": self.QUID}
                if self.QUID is "ID0":
                    out = {"output": f"{memories.soul.ID0.responseText}", "returnId": self.QUID}
                    # Note: Neko likes to mimic her
                    # creator (Ronan) and shares many feelings and
                    # memories with her.

                    # and yes I do plan to make things (a storyline)
                    # about Neko.





    # Note: i have no fucking idea if this will even work help me
    # I'm scared, Neko.
