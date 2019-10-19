class Products:

    __idProduct = 0
    __type = ""
    __name = ""
    __price = []
    __unitMeasure = ""
    __brand = ""
    __description = ""
    __stock = 0

    def __init__(self, type, name, id, price, unitMeasure, brand, description, stock):
        self.__type = type
        self.__name = name
        self.__idProduct = id
        self.__price = price
        self.__uniMeasure = unitMeasure
        self.__brand = brand
        self.__description = description
        self.__stock = stock

    def setIdProduct(self, idProd):
        self.__idProduct = idProd

    def getIdProduct(self):
        return self.__idProduct

    def setType(self, type):
        self.__type = type

    def getType(self):
        return self.__type

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def updatePrice(self, newPrice):
        self.__price.append(newPrice)

    def getPrice(self):
        return self.__price

    def setUnitMeasure(self, measure):
        self.__unitMeasure = measure

    def getUnitMeasure(self):
        return self.__unitMeasure

    def setBrand(self, brand):
        self.__brand = brand

    def getBrand(self):
        return self.__brand

    def setDescription(self, description):
        self.__description = description

    def getDescription(self):
        return self.__description

    def setStock(self, stock):
        self.__stock = stock

    def getStock(self):
        return self.__stock
