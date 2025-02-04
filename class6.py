class Moottori:
    def käynnistää(self):
        print('Moottori käynnistyy')




class Auto():
    def __init__(self) -> None:
        self.moottori = Moottori()
    def käynnistää(self):
        self.moottori.käynnistää()
        print('Auto käynnistyy')

auto = Auto()
auto.käynnistää()