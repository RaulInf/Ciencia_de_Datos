
resultado = 0

print("Pregunta 1")
p1=float(input("¿2+2?: "))
if p1 == 4:
    print ("Correcto")
    resultado += 1
else :
    print ("Respuesta Incorrecta\nRespuesta Correcta =4")


print ("--------")
print("Pregunta 2")
p2 = float(input("¿10 x 10?= "))
if p2 == 100:
    print ("Correcto")
    resultado += 1
else :
    print ("Respuesta Incorrecta\nRespuesta Correcta =100")

print ("--------")
print("Pregunta 3")
p3 = int(input("¿Edificio más alto?\n 1)Burj Khalifa  2)Torre Eiffel  = "))
if p3 == 1:
    print ("Correcto")
    resultado += 1
else :
    print ("Respuesta Incorrecta\nRespuesta Correcta = 1)Burj Khalifa")

print ("--------")
print("Pregunta 4")
p4 = float(input("¿11,952 / 4987?= "))
if p4 == 24:
    print ("Correcto")
    resultado += 1
else :
    print ("Respuesta Incorrecta\nRespuesta Correcta =24")

print ("--------")
print("Pregunta 5")
p5 = int(input("¿Rio más largo?\n 1)Misisipi  2)Nilo  = "))
if p5 == 2:
    print ("Correcto")
    resultado += 1
else :
    print ("Respuesta Incorrecta\nRespuesta Correcta = 2)Nilo")

print ("--------")
print("Pregunta 6")
p6 = int(input("¿País más grande del mundo?\n 1)Brasil  2)Rusia  = "))
if p6 == 2:
    print ("Correcto")
    resultado += 1
else :
    print ("Respuesta Incorrecta\nRespuesta Correcta = 2)Rusia")


print ("--------")
print("Pregunta 7")
p7 = int(input("¿Cuál de los 5 sentidos se desarrolla primero?\n 1)Olfato  2)Vista = "))
if p7 == 1:
    print ("Correcto")
    resultado += 1
else :
    print ("Respuesta Incorrecta\nRespuesta Correcta = 1)Olfato")


print ("--------")
print("Pregunta 8")
p8 = int(input("Atleta con más medalla olimpicas\n 1)Michael Phelps  2)Usain Bolt  = "))
if p8 == 1:
    print ("Correcto")
    resultado += 1
else :
    print ("Respuesta Incorrecta\nRespuesta Correcta = 1)Michael Phelps")


print ("--------")
print("Pregunta 9")
p9 = float(input("¿Cuánto vale PI? (dos decimales)= "))
if p9 == 3.14:
    print ("Correcto")
    resultado += 1
else :
    print ("Respuesta Incorrecta\nRespuesta Correcta = 3.14")


print ("--------")
print("Pregunta 10")
p10 = int(input("Vocalista de Queen\n 1)Michael Jackson  2)Freddie Mercury  = "))
if p10 == 1:
    print ("Correcto")
    resultado += 1
else :
    print ("Respuesta Incorrecta\nRespuesta Correcta = 2) Freddie Mercury")



print("\nTu resultado es de: %i" % resultado)
if resultado <= 4:
    print("Nivel bajo")
elif resultado > 4 <=7:
    print("Nivel promedio")
else:
    print("Nivel avanzado")