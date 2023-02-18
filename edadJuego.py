
edad=int(input("Ingrese su edad: \n"))
if 0<=edad<=4:
    print("El cliente ingresa gratis")

elif 5<=edad<=17:
    print("El valor de la entrada al juego es de $ 20.000")

elif 18<=edad<=60:
    print("El valor de la entrada al juego es de $ 15.000")

else: 
    print("El valor de la entrada al juego es de $ 3.000 ")