


  # Proposito del programa: Aplicar condicionales y reuso de funciones
# Materia:Futuros posibles: utopías y distopías en el cine y la literatura
# Autor: Jose Raul
# Fecha: 28-09-2023

#-------------------------------------------------------------------
# Esta funcion acepta el numero de pregunta a realizar
# Si la respuesta del usuario es correcta se incrementa
# la calificación del usuario

def preguntas(counter):
#Se hace uso de una variable global para llevar el conteo del score del usuario
    global resultado
    if counter == 0:
        print("Pregunta 1")
        p1=float(input("¿2+2?: "))
        if p1 == 4:
            print ("Correcto")
            resultado += 1
#La variable "resultado" contará y guardará los aciertos del usuario
        else:
            print ("Respuesta Incorrecta\nRespuesta Correcta =4")
    elif counter == 1:
        print ("--------")
        print("Pregunta 2")
        p2 = float(input("¿10 x 10?= "))
        if p2 == 100:
            print ("Correcto")
            resultado += 1
        else :
            print ("Respuesta Incorrecta\nRespuesta Correcta =100")
    elif counter ==2:
        print ("-------")
        print("Pregunta 3")
        p3 = float(input("¿Edificio más alto?\n 1)Burj Khalifa  2)Torre Eiffel  ="))
        if p3 == 1:
            print ("Correcto")
            resultado+=1
        else:
            print("Respuesta Incorrecta\nRespuesta Correcta ==1)Burj Khalifa")
    elif counter ==3:
        print ("-------")
        print("Pregunta 4")
        p4 = float(input("¿11,952 / 4987?= "))
        if p4 == 24:
            print ("Correcto")
            resultado+=1
        else:
            print("Respuesta Incorrecta\nRespuesta Correcta ==24")        
    elif counter == 4:
        print ("--------")
        print("Pregunta 5")
        p5=float(input("¿Rio más largo?\n 1)Misisipi  2)Nilo  = "))
        if p5 == 2:
            print ("Correcto")
            resultado += 1
        else:
            print ("Respuesta Incorrecta\nRespuesta Correcta =2) Nilo")
    elif counter == 5:
        print ("--------")
        print("Pregunta 6")
        p6 = float(input("¿País más grande del mundo?\n 1)Brasil  2)Rusia  = "))
        if p6 == 2:
            print ("Correcto")
            resultado += 1
        else :
            print ("Respuesta Incorrecta\nRespuesta Correcta =2)Russia")
    elif counter ==6:
        print ("-------")
        print("Pregunta 7")
        p7 = float(input("¿Cuál de los 5 sentidos se desarrolla primero?\n 1)Olfato  2)Vista  3)Tacto= "))
        if p7 == 1:
            print ("Correcto")
            resultado+=1
        else:
            print("Respuesta Incorrecta\nRespuesta Correcta ==1)Olfato")
    elif counter ==7:
        print ("-------")
        print("Pregunta 8")
        p8 = float(input("Atleta con más medalla olimpicas\n 1)Michael Phelps  2)Usain Bolt  = "))
        if p8 == 1:
            print ("Correcto")
            resultado+=1
        else:
            print("Respuesta Incorrecta\nRespuesta Correcta ==1)Michael Phelps")   
    elif counter ==8:
        print ("-------")
        print("Pregunta 9")
        p9 = float(input("¿Cuánto vale PI? (dos decimales)= "))
        if p9 == 3.14:
            print ("Correcto")
            resultado+=1
        else:
            print("Respuesta Incorrecta\nRespuesta Correcta == 3.14")
    elif counter ==9:
        print ("-------")
        print("Pregunta 10")
        p10 = float(input("Vocalista de Queen\n 1)Michael Jackson  2)Freddie Mercury  = "))
        if p10 == 2:
            print ("Correcto")
            resultado+=1
        else:
            print("Respuesta Incorrecta\nRespuesta Correcta ==2)Freddie Mercury")   
    else:
        print("No mas preguntas!")


def pregunta_bonus():
    global resultado
    print ("-----------\nPregunta Bonus")
#Aquí se crea una lista que le se mostrará al usuario
    Animales = ['Perro', 'Tortuga', 'Gato','Ballena']
    print("\n De la lista mostrada")
    print(Animales)
    bonus = input("\n¿Cual animal es oviparo? ")
#su respuesta se comparará con la lista y se obtendrá un resultado
    if bonus == Animales[1]:
        print("\n Respuesta correcta")
        resultado +=1
    else:
        print("\n Respuesta incorrecta")

#-------------------------------------------------------------------
# Declaración de variables importantes para la operación del programa
num_preguntas = 9
resultado = 0
cal_reprobatoria = 4
cal_aprobatoria = 7

#-------------------------------------------------------------------
# Ejecución de la rutina principal, la cual llama a la función 
# preguntas la cual permmite hacer las preguntas requeridas

def hacer_preguntas():
  
  global resultado
  
  for counter in range(num_preguntas):
    preguntas(counter)

  pregunta_bonus()

#Función para que haga correr los resultados del quiz
def mostrar_resultado():

  print("\nTu resultado es de: %i" % resultado)

  if resultado <= cal_reprobatoria:
    print("Nivel bajo\nSigue Practicando")
  elif resultado > cal_reprobatoria and resultado <= cal_aprobatoria:
    print("Nivel promedio\nTu puedes más")
  else:
    print("Nivel avanzado\nExcelente juego")

 # Función principal
 #Manadará a llamar los funciones de las preguntas y resultados
def main():

  hacer_preguntas()
  
  mostrar_resultado()

  
#Aqui se mostrará el score del usuario con los datos guardos en la variable "resultado"
# Fin del programa