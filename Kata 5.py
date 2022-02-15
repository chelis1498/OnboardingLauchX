primerPlaneta = 149597870
segundoPalneta = 778547200
# Calcular la distancia entre planetas

distanciaKm = primerPlaneta - segundoPalneta
print(distanciaKm)

distanciaMi = distanciaKm * 0.621
print(distanciaMi)


# Almacenar las entradas del usuario
firstPlanet = input('Introduzca la distancia del sol para el primer planeta en KM: ')
secondPlanet = input('Introduzca la distancia desde el sol para el segundo planeta en KM: ')
# Convierte las cadenas de ambos planetas a números enteros
firstPlanet = int(firstPlanet)
secondPlanet = int(secondPlanet)
# Realizar el cálculo y determinar el valor absoluto
distance_km = secondPlanet - firstPlanet
print(distance_km)

# Convertir de KM a Millas
distance_mi = distance_km * 0.621
print(abs(distance_mi))