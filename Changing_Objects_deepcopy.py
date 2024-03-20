from copy import deepcopy

# deepcopy

info = {
    'name': 'Bogdan',
    'is_instructor': True,
    'reviews': [],
}

info_deepcopy = deepcopy(info)

info_deepcopy['reviews'].append('Great course!')
info_deepcopy['reviews'].append('Super!')
info_deepcopy['new_key'] = 55
info['reviews'].append('Super')
info['new_key'] = 10

print(info)

print(info_deepcopy)