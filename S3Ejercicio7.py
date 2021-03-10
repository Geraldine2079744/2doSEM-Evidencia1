import re

nombre1="Juan Hernandez"
nombre2="Antonio Gómez"
nombre3="María López"

if re.match("antonio",nombre2, re.IGNORECASE):
    print("Se encontro nombre")
else:
    print("No se encontro nombre")
