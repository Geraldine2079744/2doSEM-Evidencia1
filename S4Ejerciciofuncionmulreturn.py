def mensaje(msg):
    print(msg)

def calcula_suma(num1,num2):
    resultado=num1+num2
    return resultado

def calcula_mul(num1,num2):
    resultado=num1*num2
    return resultado

def calcula_iva(importe,tasa):
    riva=importe*tasa
    return riva

mensaje("Suma dos numeros")
print(calcula_suma(2,3))
print(calcula_suma(7,5))
print(calcula_suma(6,1))

mensaje("Multiplica dos numeros")
print(calcula_mul(6,7))

mensaje("Calcula a importe el iva")
print(calcula_iva(100,0.16))
