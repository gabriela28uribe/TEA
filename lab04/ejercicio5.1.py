contador = 0 
suma = 0
while True: 
    try: 
        numero = input("Ingrese un número:")
        if (numero == "salir"):
            break
        else: 
            contador = contador + 1
            suma= suma + int(numero)
    except: 
        print("Debe ingresar un valor númerico")
        contador = contador - 1
        continue
print("Contador:" , contador)
print("Suma:" , suma)
print("Promedio:" , suma/contador)