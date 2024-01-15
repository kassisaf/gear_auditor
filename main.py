import os.path
from tkinter.filedialog import askdirectory


def get_windower_path() -> str:
    # TODO: Validate path and ask again if it's not Windower (look for res path?)
    return askdirectory()


def get_sets_from_gearswap_lua(filename: str):
    with open(filename, 'r') as file:
        ...
    return ''


if __name__ == "__main__":
    windower_path = get_windower_path()
    items_lua = os.path.join(windower_path, 'res', 'items.lua')
    gearswap_data_path = os.path.join(windower_path, 'addons', 'GearSwap', 'data')
    findall_data_path = os.path.join(windower_path, 'addons', 'findAll', 'data')

    if not os.path.exists(gearswap_data_path) or not os.path.exists(findall_data_path):
        print('Unable to locate either Gearswap or findAll addons in the selected path.')

    gearswap_luas = [
        os.path.join(gearswap_data_path, filename)
        for filename in os.listdir(gearswap_data_path)
        if filename.endswith('.lua')
    ]
    findall_luas = [
        os.path.join(findall_data_path, filename)
        for filename in os.listdir(findall_data_path)
        if filename.endswith('.lua')
    ]

    for gearswap_lua in gearswap_luas:
        print(gearswap_lua)
        print(get_sets_from_gearswap_lua(gearswap_lua))
        # TODO: parse sets
        # TODO: If sets were found, save key with character namegear as a set

    # for findall_lua in findall_luas:
    #     print(findall_lua)
