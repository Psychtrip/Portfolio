
# Demonatrates guards, arithmetics, and mixes between strings and numbers
def Name(n):
    global name
    name = n
    if n.isnumeric():
        print(f'Not An Accepted Name, Please Do Not Use Numbers\n')
    else:
        ans = input(f'Is {n} Correct? (Y/N) ')
        if ans == 'Y':
            print(f'\nWelcome {n}!')
            return
        else:
            Name(n=input(f'Please Enter Your Name '))

def Menu():
    print(f'\n1. Plot Type And Cost\n2. Area And Cost Of Plot\n3. Travel And Travel Cost\n4. Finalize Purchase\n5. Cancel')
    Sel = input(f'\nPlease Select One Of The Following: ')

    if Sel == '1':
        print(f'Plot Selection\nA\nB++\nC\nC++\nD')
        PlotType(Plotty=input("Please Select A Plot Type "))
        Menu()

    elif Sel == '2':
        PlotArea()
        Menu()

    elif Sel == '3':
        Travel(mi = (input ("\nPlease Input The Distance (mi): ")))
        Menu()

    elif Sel == '4':
       Total()
       Menu()

    elif Sel == '5':
        print(f'GoodBye!')
        exit()

    else:
        print(f'Not A Valid Choice, Please Try Again')
        Menu()

def PlotType(Plotty):
    PlotList = [ 'A' , 'B++' , 'C' , 'C++' , 'D']
    if Plotty in PlotList:
        print("\nAccepted Plot")
        PlotVal(Plotty)
    else:
        print("Not An Accepted Plot, Please Try Again")
        PlotType(Plotty=input("Please Select A Plot Type "))

def PlotVal(Plotty):
    global Plot
    if Plotty == 'A':
        Plot = 2.5
    elif Plotty == 'B++':
        Plot = 2
    elif Plotty == 'C':
        Plot = 1.5
    elif Plotty == 'C++':
        Plot = 1
    elif Plotty == 'D':
        Plot = 0.5
    else:
        print("Error")
        PlotType(Plotty=input("Please Select A Plot Type "))

    print(f'The Value Is 100 * {Plot} = ${100 * Plot:,.2f}\n')

def PlotArea():
    global L
    global W
    try:
        L = float(input("\nInput A Length: "))
        W = float(input("Input A Width: "))
    except ValueError:
        print("Not A Numerical Value, Please Try Again")
        PlotArea()

    print(f'\nThe Area Of The Rectangle Is {L} * {W} = {L * W:,.2f}')
    PlotCost()

def PlotCost():
    global cost
    cost = (L * W) * 1.25
    print(f'The Cost Of The Area Of The Plot (Per Square ft.) = ${cost:,.2f}\n')

def Travel(mi):
    global MiCost
    try:
        MiCost = float(mi) * 1.00
        print(f'The Cost Of {mi} Mile(s) = ${MiCost}\n')
    except ValueError:
        print("Error Please Enter A Numerical Value")
        Travel(mi = (input ("\nPlease Input The Distance (mi): ")))


def Total():
    global MiCost
    global cost
    global L
    global W
    global name
    try:
        Tax = (Plot + cost + MiCost + 125.95) * 0.0725
        Rec = open('Record.txt','w')
        Rec.write(f'RECORD\n'
              f'Name: {name}\n'
              f'Flat Fee = $125.95\n'
              f'Plot Type Cost = ${Plot:,.2f}\n'
              f'Plot Area Cost = ${cost:,.2f}\n'
              f'Travel Cost = ${MiCost:,.2f}\n'
              f'Tax = ${Tax:,.2f}\n'
              f'\nFinal Cost = ${Plot + cost + MiCost + Tax + 125.95:,.2f}\n')
    except NameError:
        print("Error: You Are Missing Data To Complete The Purchase")
        Menu()
    Rec = open('Record.txt' , 'r')
    line = Rec.readline()
    if line != '':
        Rec.readline()
    Rec.close()

if __name__ == '__main__':
    print(f'Welcome To ABC Truck Rental\nTruck Rental System')

    Name(n=input(f'\nPlease Enter Your Name '))
    Menu()


