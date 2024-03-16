# Main function for starting program
def main():
    mFileWri = open('productRec.txt', 'w')  # local variable mFileWri will open productRec.txt in write mode
    for k in range(0, 10):  # For loop repeats 10 times
        item = getItem()  # Local variable item will get return value of getItem function
        quant = getQuant()  # Local variable quant will get return value of getItem function
        price = getPri()  # Local variable price will get return value of getItem function
        # Writes into the productRec.txt file the arguments including the local variables converted into str if necessary
        mFileWri.write('Item: ' + item + ' \n')
        mFileWri.write('Quantity:' + str(quant) + ' \n')
        mFileWri.write('$' + str(price) + ' \n')


# getItem function will receive the item name
def getItem():
    # item local variable receives input and then returns it as the function's return value
    item = input("Enter grocery item: ")
    return item


# getItem function will receive the item quantity
def getQuant():
    while True:  # Keeps loop going until a valid quantity is chosen
        q = input("Enter quantity of item: ")  # q local variable will receive the input for quantity
        if q.isdigit() and q >= "0":  # If checks q as a valid quantity (positive integer or 0) and returns q as function's value return and breaks loop
            break
        else:  # If q does not satisfy valid quantity, displays error message
            print("Invalid quantity")
    return q  # Return q as the item quantity


# getItem function will receive the item price
def getPri():
    p = 0
    while True:  # Repeats until a valid item price is declared
        # Try will allow function to continue without ending the program
        try:
            p = float(input(
                "Enter price of item (rounds to 2 decimal places): "))  # local variable p will allow input for float as input
        except ValueError:
            print("Invalid price")  # If try would cause an error, prints invalid price and loop continues instead
            continue
        # If p satifies being a nonstring greater than or equal to 0, breaks loop, else prints invalid price
        if p >= 0:
            break
        else:
            print("Invalid price")
    return f'{p:,.2f}'  # Returns p as price with two decimal places


# Calls main function to execute it
if __name__ == '__main__':
    main()
