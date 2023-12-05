from OOPPracticeEIK import FoodItems
def createFoodListEIK():
    FoodList = []
    ItemNum = int(input("Please input the number of items you wish to order : "))
    for i in range(1, ItemNum + 1):
        print(f"Item #{i}-")
        FoodName = input("Please enter the food name :")
        Weight = float(input("Please enter the amount of food(in pounds) :"))
        while Weight <= 0:
            print("Please enter a valid number(bigger than 0).")
            Weight = float(input("Please enter the amount of food(in pounds) :"))
            Food_order = Food_order(FoodName,Weight)
            FoodList.append(Food_order)


def DisplayFoodListEIK(FoodList):
    for Food_order in FoodList:
        for Food_order in FoodList:
            print(f"Food Name: {Food_order.getFoodNameEIK()}")
            print(f"Amount Ordered: {Food_order.getAmountOrderedEIK()} pounds")
            print(f"Price per pound: ${Food_order.getPriceEIK():.2f}")
            print(f"Price of order: ${Food_order.getCalculatedPriceEIK():.2f}")
            print()


def TotalCalculatedPriceEIK(FoodList):
    TotalPrice = sum(Food_order.getCalculatedPriceEIK() for Food_order in FoodList)
    return TotalPrice

def main():
    ItemsList = createFoodListEIK()
    DisplayFoodListEIK(ItemsList)
    TotalPrice = TotalCalculatedPriceEIK(ItemsList)
    print(f"Total Price : ${TotalPrice: .2f}")

if __name__ == "__main__":
    main()