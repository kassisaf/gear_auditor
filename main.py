import os.path
from tkinter.filedialog import askdirectory
from typing import List
from gearswap import GearSwapLuaFile
from findall import FindAllLuaFile
from windower import WindowerResources


def get_windower_path() -> str:
    # TODO: Validate path and ask again if it's not Windower (look for res path?)
    return askdirectory()


def get_lua_filenames_from_dir(path: str) -> List[str]:
    return [os.path.join(path, filename)
            for filename in os.listdir(path)
            if filename.lower().endswith('.lua')]


if __name__ == "__main__":
    windower_path = get_windower_path()
    # windower_resources = WindowerResources(windower_path)
    gearswap_data_path = os.path.join(windower_path, 'addons', 'GearSwap', 'data')
    findall_data_path = os.path.join(windower_path, 'addons', 'findAll', 'data')

    if not os.path.exists(gearswap_data_path) or not os.path.exists(findall_data_path):
        print('Unable to locate either Gearswap or findAll addons in the selected path.')

    gearswap_luas = get_lua_filenames_from_dir(gearswap_data_path)
    findall_luas = get_lua_filenames_from_dir(findall_data_path)

    # for gearswap_lua in gearswap_luas:
    #     parsed_file = GearSwapLuaFile(gearswap_lua)
    #     print(parsed_file)
    #     print("   Equipment: ", parsed_file.get_equipment())
    #     print("   Variables: ", parsed_file.get_variables())

    for findall_lua in findall_luas:
        parsed_file = FindAllLuaFile(findall_lua)
        print(parsed_file)
