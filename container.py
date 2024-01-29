ON_PERSON_CONTAINERS = [
    'inventory',
    'satchel',
    'sack',
    'case'
]

CONTAINER_SORT_ORDER = ['inventory', 'wardrobe', 'wardrobe2', 'wardrobe3', 'wardrobe4', 'wardrobe5', 'wardrobe6',
                        'wardrobe7', 'wardrobe8', 'satchel', 'sack', 'case', 'safe', 'safe2', 'locker', 'storage',
                        'slip 01', 'slip 02', 'slip 03', 'slip 04', 'slip 05', 'slip 06', 'slip 07', 'slip 08',
                        'slip 09', 'slip 10', 'slip 11', 'slip 12', 'slip 13', 'slip 14', 'slip 15', 'slip 16',
                        'slip 17', 'slip 18', 'slip 19', 'slip 20', 'slip 21', 'slip 22', 'slip 23', 'slip 24',
                        'slip 25', 'slip 26', 'slip 27', 'slip 28', 'slip 29', 'slip 30', 'slip 31', 'key items']

# Code to regenerate list as needed:
# CONTAINER_SORT_ORDER = [
#     'inventory',
#     'wardrobe',
#     # wardrobes 2-8
#     'satchel',
#     'sack',
#     'case',
#     'safe',
#     'safe2',
#     'locker',
#     'storage',
#     # storage slips
#     'key items',
# ]
# for i in range(1, 32):
#     CONTAINER_SORT_ORDER.insert(-1, f"slip {'0' if i < 10 else ''}{i}")
# for i in range(2, 9):
#     CONTAINER_SORT_ORDER.insert(i, f'wardrobe{i}')
# print(CONTAINER_SORT_ORDER)


def is_equippable(container: str):
    return container == 'inventory' or container.startswith('wardrobe')


def is_storage(container: str):
    return container == 'storage' or container.startswith('slip')


def is_on_person(container: str):
    return container in ON_PERSON_CONTAINERS
