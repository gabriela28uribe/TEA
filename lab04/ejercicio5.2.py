máximo=0
mínimo=0
primer_numero=True
while True: 
    input_str= input("Ingrese un número: ")
    try: 
        if (input_str=='done'): 
            break
        else: 
            if (primer_numero): 
                máximo=int(input_str)
                mínimo=int(input_str)
                primer_numero= False
            else: 
                if (int(input_str)>máximo): máximo=int(input_str)
                if (int(input_str)<mínimo): mínimo=int(input_str)
    except: 
        print("Valor no válido, favor volver a intentar")
        continue
print("Máximo:", máximo)
print("Mínimo", mínimo)