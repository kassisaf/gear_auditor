import os.path
from tkinter.filedialog import askdirectory
from typing import List
from gearswap import GearSwapLuaFile
from findall import FindAllLuaFile
from windower import WindowerResources, Language
import container


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
                    character_inventories[character_name][container_name].append(item_record)

    # TODO save findall inventory in human readable format
    # TODO for each item of armor/weapon category in findall, check for presence in gearswap and mark as used/unused

    print()
