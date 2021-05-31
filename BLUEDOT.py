


__name = '__main'

planets = [
    {'Planet': 'Mercury',
     'Clasification':'Rocky planet',
     'Distance to sun': '57 910 000 Km',
     'Day duration': '58 Earth days',
     'Moons': 'None',
     },
    {'Planet': 'Venus',
     'Clasification': 'Rocky planet',
     'Distance to sun': '108 200 000 Km',
     'Day duration': '116 Earth days',
     'Moons':'None'
    }
]

def  create_planet(planet):
    global planets

    if planet not in planets:
        planets.append(planet)
    else:
        print('Planet already is in planet\'s list')


def deleate_planet(planet_name):
    global planets

    if planet_name in planets:
        planets.remove(planet_name)
    else:
        _unkwnow_planet()

def update_planet(planet, updated_planet_name):
    global planets

    for idx, planet in enumerate(planets):
        if planet['Planet'] == planet:
            planet= updated_planet_name

    else:
        return False

def search_planet(planet_name):

    for planet in planets:
        if planet['Planet'] != planet_name:
            continue
        else:
            return True

def planets_list():
    for idx, planet in enumerate(planets):
        print('{num} | {name} | {clasification} | {distance} | {day} | {moon}'.format(
            num= idx,
            name= planet['Planet'],
            clasification= planet['Clasification'],
            distance= planet['Distance to sun'],
            day= planet['Day duration'],
            moon= planet['Moons']
        ))

def _get_planet_field(fild_name):
    fild= None

    while not fild:
        fild= input ('Write planet {}: '.format(fild_name))
    return fild

def _get_planet_idx():
    return input ('Write planet index: ')

def _get_planet_name():
    return input('Write planet name: ')

def _unkwnow_planet():
    print('Unkwnow planet')




def _interfaz():
    print(' Welcome to BLUEDOT')
    print('*' * 30)
    print('What would you like to do?')

    print('[A] Add planet')
    print('[B] Deleate planet')
    print('[C] Update planet name')
    print('[D] Search planet')
    print('[E] Show planet\'s list')

if __name == '__main':
    _interfaz()

    command=input()
    command=command.upper()

                                # COMMANDS

    if command=='A':
        planet= {
        'Planet': _get_planet_field('name'),
        'Clasification': _get_planet_field('clasification'),
        'Distance to sun': _get_planet_field('distance'),
        'Day duration': _get_planet_field('day duration'),
        'Moons': _get_planet_field('moons')
        }
        create_planet(planet)
        planets_list()

    elif command=='B':
        planet_name= _get_planet_field('name')
        deleate_planet(planet_name)
        planets_list()

    elif command=='C':
        planet_name= _get_planet_name()
        found= search_planet(planet_name)

        if found:
            updated_planet_name= {
            'Planet': _get_planet_field('name'),
            'Clasification': _get_planet_field('clasification'),
            'Distance to sun': _get_planet_field('distance'),
            'Day duration': _get_planet_field('day'),
            'Moons': _get_planet_field('moons')
            }
            update_planet(planet_name, updated_planet_name)
            planets_list()
        else:
            print('Planet \'{}\' is not in planet\'s list'.format(_get_planet_field('name')))


    elif command== 'D':
        planet_name= _get_planet_name()
        found= search_planet(planet_name)

        if found:
            print('Planet is in planet\'s list')
        else:
            print('Planet \'{}\' is not in planet\'s list'.format(planet_name))

    elif command== 'E':
        planets_list()

    else:
         print('Invalid command')
