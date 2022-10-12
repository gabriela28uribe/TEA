maximo=0
minimo=0
primer_num=True
while True:
    input_str=input("Porfavor, ingrese un numero: ")
    try:
        if (input_str=='done'):
            break
        else:
            if(primer_num):
                maximo=int(input_str)
                minimo=int(input_str)
                primer_num=False
            else:
                if(int(input_str)>maximo): maximo=int(input_str)
                if(int(input_str)<minimo): minimo=int(input_str)
    except:
        print("valor no valido, favor volver a intentar :)")
        continue
print("Maximo:", maximo)
print("Minimo", minimo)