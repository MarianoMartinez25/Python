# 1) Identifica el tipo de dato (int, float, string o list) de los siguientes
# valores literales.

"Hola Mundo" #String
[10, 1, 200] #Lista de int
-30 #int
1.0 #float
["Pedro", "Jorge"] #Lista de String


# 2) Determina sin programar el resultado que aparecera en la pantalla
# a partir de las siguientes variables:
a = 20
b = 10 
c = "Pepe"
d = [1,2,3]

print(a*4) #a*4=80
print(a-b) #a-b=10
print(c+ "Garcia") #PepeGarcia
print(c*2) #c*2 = PepePepe
print(c[-1]) #c[-1]=e
print(c[1:]) #c[1:]=epe
print(d+d) #d+d=[1,2,3,1,2,3]

# 3) El siguiente codigo pretende realizar una media entre 3 numeros
# pero algo anda mal, ¿Podes identificar el problema y solucionarlo?

num_1 = 9
num_2 = 3
num_3 = 6 #el problema era que decia num-3 y no num_3
media = (num_1 + num_2 + num_3) / 3 #agregar parentesis a la suma
print("La nota media es", media)


# 4) Aqui hay otro problema, ¿Eres capaz de resolverlo? Al querer sumar entrada mas 10
# nos sale un error.¿Que es lo que esta faltando?

# entrada = int(input("Introduzca un numero: ")) #Convertir en entero
# Introduzca un numero: 20
# entrada + 10

# 5)Aqui hay un texto que esta alreves, es un alumno, que tiene una nota
# del examen.¿Como podemos darlo vuelta y verlo normalmente?

texto = "zaid luar, 01"


