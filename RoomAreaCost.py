def RoomValues():
    R1L = (float(input("Input Room 1 Length (feet) ")))
    R1W = (float(input("Input Room 1 Width (feet) ")))
    A1 = ((R1L) * (R1W))

    R2L = (float(input("\nInput Room 2 Length (feet) ")))
    R2W = float(input('Input Room 2 Width (feet) '))
    A2 = (R2L * R2W)

    R3L = float(input('\nInput Room 3 Length (feet) '))
    R3W = (float(input("Input Room 3 Width (feet) ")))
    A3 = ((R3L) * (R3W))

    AT = (A1 + A2 + A3)
    Val = (AT * 65.55)

    print(f'''
       {"Room 1 Area ":^s} {A1:>,.2f} sqft.
       {"Room 2 Area ":^s} {A2:>,.2f} sqft.
       {"Room 3 Area ":^s} {A3:>,.2f} sqft.
       {"________________________________"}
       {"Total Area = ":^s} {AT:>,.2f} sqft.
       {"Cost(sq.ft)= $":^s} {"65.55":>s}
       {"________________________________"}
       {"Value Of Area= $":^s} {Val:>,.2f} sqft.
       ''')


if __name__ == '__main__':
    RoomValues()
