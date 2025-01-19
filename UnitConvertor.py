def convert_units():
    print("Welcome to Unit Converter!")
    print("1. Celsius to Fahrenheit\n2. Kilometers to Miles\n3. Kilograms to Pounds")
    while True:
        choice = input("\nChoose an option (or type 'exit' to quit): ")
        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C = {fahrenheit}°F")
        elif choice == "2":
            km = float(input("Enter distance in Kilometers: "))
            miles = km * 0.621371
            print(f"{km} km = {miles} miles")
        elif choice == "3":
            kg = float(input("Enter weight in Kilograms: "))
            pounds = kg * 2.20462
            print(f"{kg} kg = {pounds} lbs")
        elif choice.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

convert_units()
