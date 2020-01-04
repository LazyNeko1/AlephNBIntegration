import nbutil_ao


def NOAO():
    pass


class soul:  # USED FOR AO
    class feelings:
        hurt = 0  # ( sad with slight anger)
        sad = 0  # obvious
        angered = 0  # obvious
        happy = 1  # obvious - always set to on unless one of the above is used.
        neutral = 1  # same as above
        if f"{hurt + sad + angered}" is not "000":
            happy = 0
            neutral = 0
        # how the hell do i calculate feelings
        var1, var2, var3, var4, var5, minf, maxf, maxf_override = 0, 0, 0, 0, 0, 5, 7, False  # 5-7 is neutral position, default
        if angered is 1 and hurt is 1:
            minf = 1
            maxf = 3
        if angered is 1 and sad is 1:
            minf = -4
            maxf = -1
        if hurt is 1 and sad is 1:
            minf = -10
            maxf = -5
        if neutral is 1:
            minf = 4
            maxf = 7
        if happy is 1:
            minf = 8
            maxf = 10
        # maxf = int(var1 + var2 + var3 + var4 + var5)
        # 1   2   3   4   5   6   7   8   9   10

        # 1: angered, 5:neutral, 10:happy
        # Negative scale for sadness
        if maxf_override is not False:
            maxf = maxf_override

        output = {"1": minf, "2": maxf}

    ID0 = "I remember someone like me being in that show.. Sort of ironic, isn't it?"
    cute = "Me? No, i'm not cute at all!"


class rmem:  # USED GLOBALLY ( random memories )
    # variables

    # output strings here
    def __init__(self):
        pass


class emem:  # USED INTERNALLY ( effects feelings for future)
    # variables

    # outputs
    def __init__(self):
        pass
