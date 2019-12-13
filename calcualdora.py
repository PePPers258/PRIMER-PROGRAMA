operacion = input("Bienvenido a tu pequeña gran calculadora, porfavor indica que operación quieres realizar. (multiplicar / dividir / sumar / restar): ")
primer_numero = int(input("indicame tu primer numero: "))
segundo_numero = int(input("indicame tu segundo numero: "))
if operacion == "multiplicar":
    operacion = primer_numero * segundo_numero
elif operacion == "dividir":
    operacion = primer_numero/segundo_numero
elif operacion == "sumar":
    operacion = primer_numero+segundo_numero
elif operacion == "restar":
    operacion = primer_numero-segundo_numero

resultado = operacion
print("Tu resultado es {}".format(resultado))