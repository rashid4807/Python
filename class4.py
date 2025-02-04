class Eläin:
    def __init__(self,nimi):
        self.nimi = nimi

    def ääntele(self):
        print(f'{self.nimi} ääntelee.')

class Koira(Eläin):
   def __init(self,nimi,rotu):
       super().__init__(nimi)
       self.rotu = rotu

   def ääntele(self):
       print(f'{self.nimi} ({self.rotu}) haukuuu.')
   
class Kissa(Eläin):
   def ääntele(self):
       print(f'{self.nimi} maukuu')

koira = Koira('Rex','Labradorinnoutoja')
koira.ääntele()

kissa = Kissa('Felix')
kissa.ääntele()
