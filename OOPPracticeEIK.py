class FoodItems:
    def __init__(self, FoodName, FoodWeight):
        self._FoodName = FoodName
        self._FoodWeight = int(FoodWeight)
        self._Price = 0.0
        self._CalculatePrice()
        self._CalculatedPrice = 0.0

    def CalculatePriceEIK(self):
        self.PriceListEIK()

    def PriceListEIK(self):
        if self._FoodName == 'Dry Cured Iberian Ham':
            self._Price == 177.80
        elif self._FoodName == 'Wagyu Steaks':
            self._Price == 450.00
        elif self._FoodName == 'Matsunake Mushrooms':
            self._Price == 272.00
        elif self._FoodName == 'Kopi Luwak Coffee':
            self._Price == 306.50
        elif self._FoodName == 'Moose Cheese':
            self._Price == 487.20
        elif self._FoodName == 'White Truffles':
            self._Price == 3600.00
        elif self._FoodName == 'Blue Fin Tuna':
            self._Price == 3603.00
        elif self._FoodName == 'Le Bonnotte Potatoes':
            self._Price == 270.81
        else :
            self._Price = 0.0
        FoodName = {'Dry Cured Iberian Ham': 177.80, 
                    'Wagyu Steaks': 450.00, 
                    'Matsunake Mushrooms' : 272.00, 
                    'Kopi Luwak Coffee' : 306.50, 
                    'Moose Cheese':487.20, 
                    'White Truffles':3600.00, 
                    'Blue Fin Tuna': 3603.00,
                    'Le Bonnotte Potatoes': 270.81}
    def CalculateTotalPriceEIK(self):
        self._CalculatedPrice = self._FoodWeight * self._Price
        return self._CalculatedPrice
    
    def getFoodNameEIK(self):
        return self._FoodName
    
    def getFoodWeightEIK(self):
        return self._FoodWeight
    
    def getPriceEIK(self):
        return self._Price
    
    def getCalculatedPriceEIK(self):
        return self._CalculatedPrice
    
    def __str__(self):
        return (f"Food Item: {self._FoodName}, "
            f"Weight: {self._FoodWeight} pounds, "
            f"Standard Price: {self._Price}, "
            f"Calculated Price: {self._CalculatedPrice}")
