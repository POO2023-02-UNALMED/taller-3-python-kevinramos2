class Control:
    def __init__(self):
        self.tv = None

  #enlazar tv con control.
    def setTv(self, tv):
        self.tv = tv
    def getTv(self):
        return self.tv
    def enlazar(self, tv):
        tv.setControl(self)
        self.tv = tv
      
  #metodos turnOn, turnOff, canalUp, canalDown, volumenUp, volumenDown, setCanal, getCanal.
    def turnOn(self):
        if self.tv != None:
            self.tv.turnOn()
    def turnOff(self):
        if self.tv != None:
            self.tv.turnOff()

    def canalUp(self):
        if self.tv != None:
            self.tv.canalUp()
    def canalDown(self):
        if self.tv != None:
            self.tv.canalDown()
    def setCanal(self, canal):
        if self.tv != None:
            self.tv.setCanal(canal)

    def volumenUp(self):
        if self.tv != None:
            self.tv.volumenUp()
    def volumenDown(self):
        if self.tv != None:
            self.tv.volumenDown()
    def setVolumen(self, volumen):
        if self.tv != None:
            self.tv.setVolumen(volumen)

