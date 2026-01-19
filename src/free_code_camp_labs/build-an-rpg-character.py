full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligent, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    if name == '':
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'
    
    if not isinstance(strength, int) or not isinstance(intelligent, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
    if  strength < 1 or intelligent <1 or charisma < 1:
        return 'All stats should be no less than 1'
    if  strength > 4 or intelligent > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    if strength + intelligent + charisma != 7:
        return 'The character should start with 7 points'

    str_val = strength * full_dot + (10-strength) * empty_dot
    intel_val = intelligent * full_dot + (10-intelligent) * empty_dot
    char_val = charisma * full_dot + (10-charisma) * empty_dot

    return f'{name}\nSTR {str_val}\nINT {intel_val}\nCHA {char_val}'

create_character('ren', 4, 2, 1)