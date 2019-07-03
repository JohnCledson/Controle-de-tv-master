class Tv:
    def __init__(self):
        self.status = 'Desligada'
        self.channel = 5
    def power(self):
        if self.status:
            self.status = 'Ligando'
        else:
            self.status = 'Desligando'
    def channelMore(self):
        self.channel += 1
    def channelLess(self):
        self.channel -= 1

tv = Tv()
print(tv.status)
tv.power()
print(tv.status)
print(tv.channel)
tv.channelLess()
print(tv.channel)
tv.channelMore()
print(tv.channel)