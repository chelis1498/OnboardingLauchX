planet = {
    'name' : 'Mars',
    'moons' : 2
}

print(planet["name"], 'has' , {planet["moons"]}, 'moons')

planet['circunference (km)'] = {
    'polar' : 6752,
    'equatorial' : 6792
}

print({planet["name"]}, 'has a polar circunference of', {planet["circunference (km)"]["polar"]})

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
moons = planet_moons.values()

planets = len(planet_moons.keys())

total = 0

for moon in moons:
    total = total + moon

average =total / planets

print(average)

"""planet = {
    'name': 'Earth',
    'moons': 1
}

#print(planet.get('name'))


#wibble = planet.get('wibble')# none 
#wibble = planet['wibble'] #  KeyError

planet.update({'name' : 'Makemake'})
# planet['name'] = 'Makemake'
print(planet['name'])


planet.update({
    'name': 'Jupiter',
    'moons': 79
})


planet['name'] = 'Jupiter'
planet['moons'] = 79

planet['orbital period'] = 4333

#planet.pop('orbital period')

planet ['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984

}

print({planet['name']},  'polar diameter:', {planet['diameter (km)']['polar']})

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}


if 'december' in rainfall:
      rainfall['december'] = rainfall['december'] +1
else:
    rainfall['december'] = 1


for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')


total_rainfall = 0

for value in rainfall.values():
    total_rainfall = total_rainfall + value



print(f'There was {total_rainfall}cm in the last quarter')"""
