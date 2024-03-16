def PizzaTime():
    AreaCost = 0.55  # price per unit
    PiTop = 1.25  # price per topping
    ConArea = 3.1414  # Constant Area (pi)
    TaxRate = 0.085  # Tax rate
    ConRad = 1.15  # Constant Radius

    PiSize = int(input("""
1 = Small
2 = Medium
3 = Large
Input Desired Pizza Size: """))  # Asks For The Users Pizza Size

    Radius = (PiSize * ConRad)  # Calc. Radius of Pizza (Users Desired Pizza Size x Constant Area (pi))
    PiArea = (Radius ** 2 * ConArea)  # Calc. Area Of Pizza (Radius Of Pizza Squared Times The Constant Area)

    TopNum = int(input("\nEnter Desired Amount Of Toppings: "))  # Asks For Number Of Toppings
    NumPizza = int(input("\nEnter Desired Amount of Pizzas: "))  # Asks For Number Of Pizzas

    PizzaPrice = ((PiArea * AreaCost) * NumPizza)  # Calc. Total Pizza Pricing
    TopPrice = ((TopNum * PiTop) * NumPizza)  # Calc. Total Price Of Toppings
    SalePrice = (PizzaPrice + TopPrice)  # Calc. Sales Price
    Tax = (SalePrice * TaxRate)  # Calc. Sales Tax
    TotalPrice = (SalePrice + Tax)  # Calc. Total Amount

    print(f'''
Pizza Area Price= ${PizzaPrice:,.2f}
Topping Price= ${TopPrice:,.2f}
Sale Price= ${SalePrice:,.2f}
Tax= ${Tax:,.2f}
______________________________
Total= ${TotalPrice:,.2f}
    ''')  # Displays Answers To Final Calculations
    quit()


if __name__ == '__main__':
    PizzaTime()
