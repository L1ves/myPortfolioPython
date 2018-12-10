def get_formated_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formated_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, middle_name, last_name):
    """Возвращает аккуратно отформатированное полное имя."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

def get_formatted_name(first_name, last_name, middle_name = ' '):
    """Возвращает аккуратно отформатированное полное имя."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formated_name('jimi', 'hendrix')
print(musician)
musician = get_formated_name('john', 'hooker', 'lee')
print(musician)
