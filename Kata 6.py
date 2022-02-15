planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planets.append('Pluton')
cantPlanets = len(planets)
print('Numero de planetas: ', cantPlanets,  '\nEl ultimo planeta es: ', planets[-1])

uInput = input('Ingrese el nombre de un planeta: ')
indice = planets.index(uInput)
print('Los planetass mas cercanos son: ', planets[0:indice])
print('Los planetas mas alejados son: ', planets[indice + 1:])