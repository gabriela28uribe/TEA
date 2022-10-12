def calculo_cal(grade):
    if (grade>=0.9 and grade<=1.0):
      grade="Sobresaliente"
    elif (grade>=0.8 and grade<=0.9):
      grade="notable"
    elif (grade>=0.7 and grade<=0.8):
      grade="bien"
    elif (grade>=0.6 and grade<=0.7):
      grade="Suficiente"
    elif (grade>=0 and grade<=0.6):
      grade="Insuficiente"
    else:
      print("Calificacion no valida")
    return grade
try:
    score = float(input("introduzca una puntuacion entre 0.0 y 1: "))
    grade = calculo_cal(score)
    print("El grado de su calificacion es:", grade)
except:
    print("caracter no valido")