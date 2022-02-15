#def reporte(principal, externo, hidrogeno):
#    total_average = (principal + externo + hidrogeno) / 3"""
 #   return f"""Fuel Report: Porcentaje: {total_average}%  Principal: {principal}%  Externo: {externo}%  Hidrogeno: {hidrogeno}%"""

#print(reporte(80, 70, 85))

def promedio(values):
    total = sum(values)
    number_of_items = len(values)
    return total / number_of_items

print(promedio([80, 85, 81]))

#def reporte(principal, externo, hidrogeno):
#    return f"""Reporte de combustible: Promedio total: {promedio([principal, externo, hidrogeno])}%
#    Principal: {principal}%
#    Externo: {externo}%
#    Hidrogeno: {hidrogeno}% 
#    """

#print(reporte(88, 76, 70))


#def reporte_mision(destino, *minutes, **fuel_reservoirs):
#   return f"""
#   Vuelo hacia {destino}
#    Tiempo de viaje: {sum(minutes)} minutos
#    Combustible: {sum(fuel_reservoirs.values())} gallons
#    """

#print(reporte_mision("Moon", 10, 15, 51, main=300000, external=200000))

def reporte_mision(destino, *minutes, **fuel_reservoirs):
    principal = f"""
    Vuelo hacia {destino}
    Tiempo de viaje: {sum(minutes)} minutos
    Combustible: {sum(fuel_reservoirs.values())} gallons
    """
    for tanque, combustible in fuel_reservoirs.items():
        principal += f"{tanque} tanque = {combustible} galones restantes\n"
    return principal

print(reporte_mision("Moon", 8, 11, 55, main=300000, external=200000))

"""# Defino mi función
def rocket_parts():
    print('payload, propellant, structure')

 # Llamo a mi función

rocket_parts()

output = rocket_parts()
print(output is None)

def distance_from_earth(destination):
    if destination == 'Moon':
        return '238,855'
    else:
        return 'Unable to compute to that destination'

#distance_from_earth()
print(distance_from_earth('Saturn'))

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

print(days_to_complete(238855, 75))
print(round(days_to_complete(238855, 75)))

from datetime import timedelta, datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f'{destination} Arrival: %A %H:%M')

print(arrival_time('Orbit', hours=0.13))

def variable_length(*args):
    print(args)

variable_length('one', 'two')

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f'Total time to launch is {total_minutes} minutes'
    else:
        return f'Total time to launch is {total_minutes/60} hours'

print(sequence_time(4, 14, 48))

def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day='Wednesday', pilots=3)


def crew_members(**kwargs):
    print(f'{len(kwargs)} astronauts assigned for this mission:')
    for title, name in kwargs.items():
        print(f'{title}: {name}')

crew_members(captain='Neil Armstrong', pilot='Buzz Aldrin', command_pilot='Michael Collins')"""