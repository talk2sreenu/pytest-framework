
def add_setting(dictionary, settings):
    key_value = settings[0].lower()
    set_value = settings[1].lower()

    if key_value in dictionary.keys():
        return f"Setting '{key_value}' already exists! Cannot add a new setting with this name."
    dictionary[key_value] = set_value
    return f"Setting '{key_value}' added with value '{set_value}' successfully!"

def update_setting(dictionary, settings):
    key_value = settings[0].lower()
    set_value = settings[1].lower()

    if not key_value in dictionary.keys():
        return f"Setting '{key_value}' does not exist! Cannot update a non-existing setting."
    
    dictionary[key_value] = set_value
    return f"Setting '{key_value}' updated to '{set_value}' successfully!"

def delete_setting(dictionary, key):
    key_value = key.lower()
    if not key_value in dictionary.keys():
        return 'Setting not found!'
    del dictionary[key_value]
    return f"Setting '{key}' deleted successfully!"

def view_settings(dictionary):
    settings = 'Current User Settings:\n'
    if not dictionary:
        return 'No settings available.'
    if dictionary:
        for key, value in dictionary.items():
            settings += f'{key.capitalize()}: {value}\n'
    return settings

test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
print(view_settings(test_settings))
print(view_settings({}))