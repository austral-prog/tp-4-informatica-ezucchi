def leap_year():
    year = float(input("Ingrese un año: "))
    if float(year / 400) == int(year / 400) and float(year / 4) == int(year / 4):
        print(f"El año {int(year)} es bisiesto")
    else:
       print(f"El año {int(year)} no es bisiesto")
