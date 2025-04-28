"""
fill the dictionary with actual uni buildings and additional key:value pairs if necessary

add more energy information
(I've just used random numbers, but you could consider building size, opening/closing times etc.
to calculate a more accurate energy measurement)

update rating if/else statements with more accurate conditions

provide better feedback to users
(maybe it could give specific building recommendations or provide energy saving tips?)

link function back to main.py

I haven't used OOP here so there are no classes/objects yet
"""

#dictionary of buildings, including their department and energy info

building_dict = {
    'building_1' : {
        'name': 'classrooms',
        'department': 'maths',
        'energy': 10
    },
    'building_2' : {
        'name': 'library',
        'department': 'general',
        'energy': 80
    },
    'building_3' : {
        'name': 'hall',
        'department': 'general',
        'energy': 50
    },
    'building_4' : {
        'name': 'laboratory',
        'department': 'chemistry',
        'energy': 170
    },
    'building_5' : {
        'name': 'computer rooms',
        'department': 'computer science',
        'energy': 200
    }
}


def select_building():

# function compiles list of departments, removing any duplicates

    department_list = []
    for item in building_dict:
        department_list.append(building_dict[item]['department'])


    for department in department_list:
        i = department_list.index(department) + 1
        while i < len(department_list):
            if department == department_list[i]:
                department_list.remove(department_list[i])
            else:
                i += 1
    department_list = sorted(department_list)

#function presents summarised list of departments, asks user to select one

    print('Here are the departments in the university:')
    i = 1
    for item in department_list:
        print(f'{i}. {item}')
        i += 1
    selection = input('Which department do you want to look at?')

#function presents list of buildings from selected department, asks user to select one
    if selection in department_list:
        print(f'Here are the buildings from the {selection} department:')

        building_list = []
        for item in building_dict:
            if building_dict[item]['department'] == selection:
                building_list.append(building_dict[item]['name'])
        building_list = sorted(building_list)

        i = 1
        for item in building_list:
            print(f'{i}. {item}')
            i += 1

        selection2 = input('which building do you want to look at?')

        if selection2 not in building_list:
            print(f'Sorry, building not recognised. Please try again.')
            print('......................................................')
            return select_building()

    else:
        print(f'sorry, department not recognised. Please try again.')
        print('...........................................................')
        return select_building()

#selected building is given energy grade (colour) based on energy usage

    for item in building_dict:
        if building_dict[item]['name'] == selection2:
            energy = building_dict[item]['energy']
            print(f'{selection2} uses up {energy} kW of energy each day.')

    if energy <= 50:
        print(
            f'ENERGY RATING: GREEN \n'
            f'{selection2} is an energy efficient building. \n'
            f'We recommend using it as much as possible!'
        )
    elif energy > 50 and energy <= 150:
        print(
            f'ENERGY RATING: YELLOW \n'
            f'{selection2} is a somewhat energy efficient building. \n'
            f'Using this building is fine, but we recommend '
            f'looking for more efficient alternatives, if possible'
        )
    else:
        print(
            f'ENERGY RATING: RED \n'
            f'{selection2} is not an energy efficient building. \n'
            f'We recommend avoiding/limiting time in buildings like this.'
              )


select_building()