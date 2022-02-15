
from click import echo
from matplotlib.pyplot import title
from zmq import PROTOCOL_ERROR_ZAP_INVALID_METADATA


text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

formato = text.split()

palabrasClave = ['average', 'temperature', 'distance']

#for palabra in formato:
#    for key_word in palabrasClave:
#        if key_word in palabra:
#            print(palabra)
#            break

for palabra in formato:
    for key_word in palabrasClave:
        if key_word in palabra:
            print(palabra.replace(' C', ' Celsius'))
            break

name = 'Moon'
gravity = 0.00162
planet = 'Earth'

title = f'La gravedad en {name}'

hechos = f"""{'-'*80}
Nombre del planeta: {planet}
Graved en {name}: {gravity * 1000}m/s2
"""
plantilla = f"""{title.title()}
{hechos}
"""
print(hechos)

planeta = 'Marte'
gravedad = 0.00143
nombre = 'Ganimedes'

print(hechos)

nuevaPlantilla = """Datos de Gravedad sobre: {nombre}
-------------------------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""

print(nuevaPlantilla.format(nombre = nombre, planeta = planeta, gravedad = gravedad))

print(nuevaPlantilla.format(nombre=nombre, planeta=planeta, gravedad=gravedad*1000))