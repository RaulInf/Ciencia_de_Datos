
def pregunta(suma):
    if suma ==4:    
        return ("Corecto") 
        
    
    else :
        return ("Respuesta Incorrecta\nRespuesta Correcta =4")    
    
suma=int(input("¿Cuanto es 2+2? "))
print (pregunta(suma))


    



print ("--------")
def pregunta2 (mult):
    if mult==100:
        return "Correcto"
    else:
        return ("Respuesta Incorrecta\nRespuesta Correcta =100")
    
mult=int(input("¿10 x 10? "))
print (pregunta(mult))

    

print ("--------")
def pregunta3(altura):
    if altura == 1:
        return "Correcto"
    else:
        return ("Respuesta Incorrecta\nRespuesta Correcta = 1)Burj Khalifa")

altura=int(input("¿Edificio más alto?\n 1)Burj Khalifa  2)Torre Eiffel  ="))
print (pregunta(altura))



print ("--------")
def pregunta4(veinticuatro):
    if veinticuatro==24:
        return "Correcto"
    else:
        return ("Respuesta Incorrecta\nRespuesta Correcta =24")
    
veinticuatro=int(input("¿11,952 / 4987?="))
print (pregunta(veinticuatro))

