from termcolor import colored

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print(colored("Eres mayor de edad.", "green"))
else:
    print(colored("Eres menor de edad.", "red"))
