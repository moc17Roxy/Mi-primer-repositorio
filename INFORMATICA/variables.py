#Esto es un  comentario de una sola linea 
""" Esto es un comentrio de
 varias lineas """

#inicializando variables 
Nombre="Keyner Stick Acuña Muñoz"
Edad= 15
Estado=True
Nota=5.0

#Mostrar el contenido de las variebles print()
print(Nombre)
print(Edad)
print(Estado)
print(Nota)

#Que tipo de dato tiene cada variable.
print(type(Nombre))
print(type(Edad))
print(type(Estado))
print(type(Nota))

#vamos a utilizar la fumcion input para recoger datos por medio del teclado
Nombre=input("¿como te llamas?")
Edad=input("que edad tienes?")
estado=input("¿en que estado te encuentras?")
Nota=input("cual es tu nota?")

#para visualizar que guardamos en las variables anteriores 
print("hola,",Nombre,"un gusto conocerte")
print("tu edad es:",Edad)
print("tu estado es:",Estado)
print("tu nota es:",Nota)