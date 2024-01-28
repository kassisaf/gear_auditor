ON_PERSON_CONTAINERS = [
    'inventory',
    'satchel',
    'sack',
    'case'
]


def is_equippable(container: str):
    return container == 'inventory' or container.startswith('wardrobe')


def is_storage(container: str):
    return container == 'storage' or container.startswith('slip')


def is_on_person(container: str):
    return container in ON_PERSON_CONTAINERS
