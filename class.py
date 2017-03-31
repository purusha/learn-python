class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    @staticmethod
    def for_you(you):
        print(you * 6)

    @classmethod
    def for_other(clazz, other):
        print(clazz)
        print(other * 6)

    def for_me(self, name):
        for line in self.lyrics:
            print("song [%s] for [%s]" %(line, name))

s = Song(["say me baby", "find me when you are loss", "call me"])
s.for_me("Alan")
s.for_you("RRRRRR")
#print(dir(s))

Song.for_you("XXX")
Song.for_other("YYY")
