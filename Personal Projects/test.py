#Pregunta nombre
nombreinicial = "Diego"
nombrerecibido = input ("Yo se quien eres pero quiero que me digas: Quién eres?\n")

varsinceridad = nombreinicial == nombrerecibido
if varsinceridad == True:
    print("Sabría que dirías la verdad", nombrerecibido) 
else:
    print("Hola", nombrerecibido+ ", estoy buscando a", nombreinicial+".")
#Acaba primera prueba

#Pregunta la edad de nombreinicial 
if varsinceridad == True:
    inputedad = input ("Cuántos años tienes?\n")
    edad = int(inputedad)
    try:
        if edad <= 18:
            mayoria = 18 - edad
            print("Faltan", mayoria, "años para que seas mayor de edad")
        else:
            print("Felicidades ya eres mayor de edad")
            overage = edad - 18
            print("Desde hace", overage, "años eres mayor de edad! Tienes", inputedad, "años de edad.")
    except:
        print("Recuerda poner un número")
else:
    print("Búscame a", nombreinicial)