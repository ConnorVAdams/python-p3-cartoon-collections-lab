def roll_call_dwarves(dwarves):
    for dwarf in dwarves:
        print(f'{dwarves.index(dwarf) + 1}. {dwarf}')

def summon_captain_planet(list):
    return [f'{item.title()}!' for item in list]

def long_planeteer_calls(list):
    for item in list:
        if len(item) > 4:
            return True
    return False

def find_the_cheese(list):
    for item in list:
        if item == 'cheddar':
            return item
        
