import math

# Pedimos al usuario los 2 datos que necesitamos
angulo_lanz = input("Por favor ingrese el angulo de lanzamiento en grados :")
veloci_lanz = input("Por favor ingrese la velocidad de lanzamiento en Km/h:")

# Declaro las variables en cero para despues ser utilizadas
tiempo_max = 0
altura_max = 0
permanencia = 0
df = 0
velocidad_x = 0
velocidad_y = 0
gravedad = 9.8


# se ingresan las formulas
velocidad_x = (veloci_lanz * math.cos(angulo_lanz))
velocidad_y = (veloci_lanz * math.sen(angulo_lanz))

df = (2 * veloci_lanz**2 * math.cos(angulo_lanz)) / gravedad * math.tan(angulo_lanz)
tiempo_max = 2 * veloci_lanz * math.seno(angulo_lanz)

altura_max = (veloci_lanz**2 * math.seno(angulo_lanz)**2) / 2 * gravedad



# Armo la respuesta que le voy ha mostrar al usuario

res = "Altura maxima de la tecnica es : " + str(tiempo_max) + "\n"
res = res + "Altura Maxima Kame Hame Ha es :"+str(altura_max)+"\n"
res = res + "al llega al suelo la distancia es :"+str(df)+"\n"
res = res + "Velocidad en X es :"+str(velocidad_x)+"\n"
res = res + "Velocidad en Y es :"+str(velocidad_y)+"\n"


# muestro la respuesta al usuario
print(res)
