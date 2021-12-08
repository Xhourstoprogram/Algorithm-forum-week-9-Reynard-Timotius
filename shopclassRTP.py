class ShopListRTP:
    def __init__(self,name,amount):
        self.__name = name
        self.__amount = amount
        self.__normalprice = self.getnormalprice()
        self.__calculateprice = self.getcalculateprice()
    
    def __pricelistRTP(self):
        if self.__name == "Dry Cured Iberian Ham":
            self.__normalprice = 177.80
        elif self.__name == "Wagyu Steaks":
            self.__normalprice = 450.00
        elif self.__name == "Matsutake Mushrooms":
            self.__normalprice = 272.00
        elif self.__name == "Kopi Luwak Coffee":
            self.__normalprice = 306.50
        elif self.__name == "Moose Cheese":
            self.__normalprice = 487.20
        elif self.__name == "White Truffles":
            self.__normalprice = 3600.00
        elif self.__name == "Blue Fin Tuna":
            self.__normalprice = 3603.00
        elif self.__name == "Le Bonnotte Potatoes":
            self.__normalprice = 270.81
        else:
            self.__normalprice = 0.00

    def getname(self):
        return self.__name

    def getamount(self):
        return self.__amount

    def getnormalprice(self):
        self.__pricelistRTP
        return self.__normalprice

    def getcalculateprice(self):
        self.__calculateprice = self.__amount * self.getnormalprice()
