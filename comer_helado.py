apetece_helado_input = input("¿Tienes ganas de una nieve? (Si / No)  ")
tienes_dinero_input = input("¿Tienes dinero para comprarlo? (Si / No)  ")
local_nieves_input = input("¿Estás cerca del local de las nieves? (Si / No)  ")
tu_mama_paga_input = input("¿Está tu mamá para pagarlo? (Si / No)  ")

apetece_helado = apetece_helado_input == "Si"
tienes_dinero = tienes_dinero_input == "Si" or tu_mama_paga_input == "Si"
local_nieves = local_nieves_input == "Si"
tu_mama_paga = tu_mama_paga_input == "Si"

if apetece_helado and tienes_dinero and local_nieves:
    print("Que disfrutes tu nieve")
else:
    print("Que mala suerte, sera para la próxima")