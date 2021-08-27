# Operador not
# print(not True)

# Operador and
# print(True and False)

# Operador or
# print (True or False)

c = "Phyton"
print(len(c) < 8 and c[0] == "P")

kil = int(input("A cuantos kilometros se encuentra de la escuela?: "))
her = int(input("Cuantos hermanos tiene en la escuela?: "))
ing = int(input("De cuanto es el ingreso en su casa?: "))

if kil < 10 and her < 2 or ing > 2000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")
