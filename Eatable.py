from Products import Products


class Eatable(Products):

    __expirationDate = ""

    def __init__(self, type, name, id, price, unitMeasure, brand, description, stock, date):

        Products.__init__(self, type, name, id, price, unitMeasure, brand, description, stock)
        self.__expirationDate = date


    def setExpirationDate(self, date):
        self.__expirationDate = date

    def getExpirationDate(self):
        return self.__expirationDate
