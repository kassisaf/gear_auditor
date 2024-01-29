import os.path
from tkinter.filedialog import askdirectory
from typing import List

from modules.findall import FindAllLuaFile
from modules.gearswap import GearSwapLuaFile
from modules.windower import WindowerResources

EQUIPPABLE_ITEM_CATEGORIES = ['Weapon', 'Armor']


def get_windower_path() -> str:
    # TODO: Validate path and ask again if it's not Windower (look for res path?)
    return askdirectory()


def get_lua_filenames_from_dir(path: str) -> List[str]:
    return [os.path.join(path, filename)
            for filename in os.listdir(path)
            if filename.lower().endswith('.lua')]


if __name__ == "__main__":
    windower_path = get_windower_path()
    windower_resources = WindowerResources(windower_path)
    gearswap_data_path = os.path.join(windower_path, 'addons', 'GearSwap', 'data')
    findall_data_path = os.path.join(windower_path, 'addons', 'findAll', 'data')

    if not os.path.exists(gearswap_data_path) or not os.path.exists(findall_data_path):
        print('Unable to locate either Gearswap or findAll addons in the selected path.')

    # Parse GearSwap and FindAll luas
    parsed_gearswap_luas = []
    parsed_findall_luas = []
    for gearswap_lua_filename in get_lua_filenames_from_dir(gearswap_data_path):
        parsed_gearswap_luas.append(GearSwapLuaFile(gearswap_lua_filename))
    for findall_lua_filename in get_lua_filenames_from_dir(findall_data_path):
        parsed_findall_luas.append(FindAllLuaFile(findall_lua_filename))

    # Compile a list of character inventory items
    character_inventories = {}
    for findall_lua in parsed_findall_luas:
        character_name = findall_lua.get_character_name()
        character_inventories[character_name] = {}

        for container_name, item_dict in findall_lua.get_items().items():
            if len(item_dict) > 0:
                character_inventories[character_name][container_name] = []

            for item_id, quantity in item_dict.items():
                item = windower_resources.get_item_by_id(item_id)
                if item is None:
                    print(f"Warning: found unknown item id {item_id} in {character_name}'s {container_name}")
                else:
                    item_record = {
                        'item': item,
                        'quantity': quantity,
                        'used_in_gearswap': False
                    }

                    # Look for item in GearSwap luas
                    if item['category'] in EQUIPPABLE_ITEM_CATEGORIES:
                        for gearswap_lua in parsed_gearswap_luas:
                            if not gearswap_lua.applies_to_character(character_name):
                                continue
                            if gearswap_lua.contains_item(item):
                                item_record['used_in_gearswap'] = True
                                break

                    character_inventories[character_name][container_name].append(item_record)

    # TODO save findall inventory in human readable format

    print("\nStart of GearSwap audit:\n=========================")
    for character, inventory in character_inventories.items():
        print(character)
        print("Equippable items not found in gearswap:")
        for container_name in inventory:
            if 'slip' in container_name or container_name == 'key items':
                continue
            print(' ' * 2, container_name)
            for item_record in inventory[container_name]:
                if item_record['item']['category'] in EQUIPPABLE_ITEM_CATEGORIES and not item_record['used_in_gearswap']:
                    print(' ' * 4, item_record['item']['enl'])
    print()
