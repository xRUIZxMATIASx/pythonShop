from Products import Products


class NonEatable(Products):

    __colour = ""

    def __init__(self, type, name, id, price, unitMeasure, brand, description, stock, color):
        Products.__init__(self, type, name, id, price, unitMeasure, brand, description, stock)
        self.__colour = color

    def setColour(self, colour):
        self.__colour = colour

    def getColour(self):
        return self.__colour
