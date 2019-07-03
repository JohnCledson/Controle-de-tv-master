class Tv:
    def __init__(self):
        self.status = 'Desligada'
    def power(self):
        if self.status:
            self.status = 'Ligando'
        else:
            self.status = 'Desligando'

tv = Tv()
print(tv.status)
tv.power()
print(tv.status)