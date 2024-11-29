from Vehicle import Car, Motorcycle, Truck

while True:
    menu = int(input("1 - Car\n2 - Motorcycle\n3 - Truck\nEnter the vehicle type: "))
    mark = input("Enter the vehicle brand: ")
    model = input("Enter the vehicle model: ")
    fuel = (input("Which fuel: "))
    capacity = (input("What capacity: "))
    
    if menu == 1:
        Vehicle = Car(mark, model)
        print(f"Type vehicle:{menu},\nMark:{mark}\nModel:{model}\nFuel type:{fuel}\nCapacity:{capacity} people.")  
    elif menu == 2:
        Vehicle = Motorcycle(mark, model)
        print(f"Type vehicle:{menu},\nMark:{mark}\nModel:{model}\nFuel type:{fuel}\nCapacity:{capacity} people.")
    elif menu == 3:
        Vehicle = Truck(mark, model)
        print(f"Type vehicle:{menu},\nMark:{mark}\nModel:{model}\nFuel type:{fuel}\nCapacity:{capacity} people.")
    else:
        print("invalid option")
