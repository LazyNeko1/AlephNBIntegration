# Basic UTILS file for the Aleph Integration. Modified version of NBUTILs (pypi)

import os
import aiohttp

#Main File
import nekoBot_alephintegration as nb

class NekoBot():
    Fname="Neko"
    Mname="Bot"
    Lname="Cheliese"
    Fullname=f"{Fname} {Mname} {Lname}"
    def __init__(self):
        self.Fullname=Fullname
        

class HTTP():
    osNam = os.name
    osSys = os.system
    def __init__(self, headers, url, timeFrame=0):
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

    class get():
        def __init__(self, UUID=0, UNAME=None):
            self.UUID = UUID
            self.UNAME = UNAME

        def UserStats_FROMID(self):
            if self.UUID is 0 or None:
                return f"Could not get User Info from ID {self.UUID}"
            if self.UUID is not 0 or None:
                OUT = None
                return OUT
        def UserStats_FROMNAME(self):
            pass
