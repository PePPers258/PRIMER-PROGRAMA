nuemro_inicial = 10
print(nuemro_inicial)
if nuemro_inicial % 2 == 0:
    print("Este número es par")
else:
    print("Este número es inpar")

while nuemro_inicial > 0:
    nuemro_inicial -= 1
    print (nuemro_inicial)
    if nuemro_inicial % 2 == 0:
        print("Este número es par")
    else:
        print("Este número es inpar")
print("He términado")
