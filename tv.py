class Tv:
    def __init__(self):
        self.status = 'Desligada'
        self.channel = 5
    def power(self):
        if self.status == 'Desligada':
            self.status = 'Ligado'
        else:
            self.status = 'Desligada'
    def channelMore(self):
        if self.status == 'Ligado':
            self.channel += 1
    def channelLess(self):
        if self.status == 'Ligado':
            self.channel -= 1
    def channelGoTo(self, num):
        if self.status == 'Ligado':
            self.channel = num

tv = Tv()
print(tv.status)
tv.power()
print(tv.status)
print(tv.channel)
tv.channelLess()
print(tv.channel)
tv.channelMore()
print(tv.channel)
tv.channelGoTo(35)
print(tv.channel)
tv.power()
print(tv.status)
tv.channelGoTo(24)
print(tv.channel)