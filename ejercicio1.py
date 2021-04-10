#1. Escribe un programa Python que acepte el radio de un círculo del usuario y calcule el área.

from math import pi

radio = float(input("Escribe el radio del círculo:"))

area = pi*radio**2

print("El área del círculo es:", area)
