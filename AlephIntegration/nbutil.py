import aiohttp


class HTTP():
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
        def UserStats_FROMNAME(self):
            pass