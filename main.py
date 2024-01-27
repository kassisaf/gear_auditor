import os.path
import re
from tkinter.filedialog import askdirectory
from typing import List

LUA_COMMENT_OPERATOR = '--'
EMPTY_SLOT = 'empty'
EQUIPMENT_SLOTS = [
    'main',
    'sub',
    'range',
    'ammo',
    'head',
    'body',
    'hands',
    'legs',
    'feet',
    'left_ear',
    'right_ear',
    'left_ring',
    'right_ring',
    'back',
    'neck',
    'waist',
]
GEARSWAP_AUGMENTED_ITEM_DEFINITION = r'{\s*(name)=\s*"(.+)",\s*augments\s*='
GEARSWAP_SLOT_DEFINITION = f"({'|'.join([f'({slot})' for slot in EQUIPMENT_SLOTS])})" + r"\s*=\s*"


def get_windower_path() -> str:
    # TODO: Validate path and ask again if it's not Windower (look for res path?)
    return askdirectory()


def is_quoted(string: str) -> bool:
    return (string.startswith("'") and string.endswith("'")) or (string.startswith('"') and string.endswith('"'))


def remove_surrounding_quotes(string: str) -> str:
    if len(string) >= 3 and is_quoted(string):
        return string[1:-1]
    return string


def get_character_name_from_gearswap_lua(filename_without_path: str):
    filename_split_by_underscore = filename_without_path.split('_')
    if len(filename_split_by_underscore) == 2:
        job_maybe, file_ext = os.path.splitext(filename_split_by_underscore[1])
        if len(job_maybe) == 3 and job_maybe.isupper():
            return filename_split_by_underscore[0]
    return None


def get_equipment_from_gearswap_lua(filename: str):
    result = {
        'filename': None,
        'character_name': None,
        'equipment': [],
        'variables': []
    }

    filename_without_path = os.path.split(filename)[-1]
    result['filename'] = filename_without_path
    result['character_name'] = get_character_name_from_gearswap_lua(filename_without_path)

    with open(filename, 'r') as file:
        for line in file:
            if line.strip().startswith(LUA_COMMENT_OPERATOR):
                continue

            if re.search(GEARSWAP_SLOT_DEFINITION, line):
                terms = [term.strip().replace(',', '') for term in line.split('=')]
                if len(terms) >= 2 and terms[1] != EMPTY_SLOT:
                    terms[1] = terms[1].split(LUA_COMMENT_OPERATOR)[0].strip()  # remove trailing comments
                    if is_quoted(terms[1]):
                        unquoted = remove_surrounding_quotes(terms[1])
                        if len(terms[1]) > len(unquoted):
                            result['equipment'].append(unquoted)
                    else:
                        # TODO: Attempt to look up variable's item name
                        # if re.search(GEARSWAP_AUGMENTED_ITEM_DEFINITION, line):
                        result['variables'].append(terms[1])
    return result


def get_lua_filenames_from_dir(path: str) -> List[str]:
    return [os.path.join(path, filename)
            for filename in os.listdir(gearswap_data_path)
            if filename.lower().endswith('.lua')]


if __name__ == "__main__":
    windower_path = get_windower_path()
    items_lua = os.path.join(windower_path, 'res', 'items.lua')
    gearswap_data_path = os.path.join(windower_path, 'addons', 'GearSwap', 'data')
    findall_data_path = os.path.join(windower_path, 'addons', 'findAll', 'data')

    if not os.path.exists(gearswap_data_path) or not os.path.exists(findall_data_path):
        print('Unable to locate either Gearswap or findAll addons in the selected path.')

    gearswap_luas = get_lua_filenames_from_dir(gearswap_data_path)
    findall_luas = get_lua_filenames_from_dir(findall_data_path)

    for gearswap_lua in gearswap_luas:
        print(get_equipment_from_gearswap_lua(gearswap_lua))
        # TODO: parse sets
        # TODO: If sets were found, save key with character namegear as a set

    # for findall_lua in findall_luas:
    #     print(findall_lua)
