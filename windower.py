import os
import re
from enum import Enum
from typing import Optional
from helpers import remove_surrounding_quotes

ITEM_LINE_PATTERN = r"^\s*\[\d+\] = {(.+)},$"
NUMERIC_ITEM_PROPS = [
    'id',
    'flags',
    'stack',
    'targets',
    'cast_time',
    'jobs',
    'level',
    'races',
    'slots',
    'cast_delay',
    'max_charges',
    'recast_delay',
    'shield_size',
    'damage',
    'delay',
    'skill',
    'item_level',
    'superior_level'
]
STRING_ITEM_PROPS = [
    'en',
    'ja',
    'enl',
    'jal',
    'category',
    'type',
    'ammo_type',
    'range_type',
]


class Language(Enum):
    ENGLISH = 'en',
    ENGLISH_FULL = 'enl',
    JAPANESE = 'ja',
    JAPANESE_FULL = 'jal',


class WindowerResources:
    def __init__(self, windower_path: str):
        self._path = windower_path
        self._items = {}

        self._parse_items_resource_file()

    def _parse_items_resource_file(self):
        items_lua = os.path.join(self._path, 'res', 'items.lua')
        with open(items_lua, 'r', encoding='utf8') as file:
            for line in file:
                # Look for lines with item definitions
                match = re.match(ITEM_LINE_PATTERN, line)
                if match:
                    # Build an item dict from the current line's lua table
                    item_props = match.group(1).split(',')
                    item = {}
                    for i, prop in enumerate(item_props):
                        try:
                            key, value = prop.split('=')
                            item[key] = value
                        except ValueError:
                            # Deal with items with commas in their name (10k bynes, rem's tales)
                            if '=' not in prop:
                                # If no = found in the current "prop", append to previous prop's value
                                previous_key, previous_value = item_props[i - 1].split('=')
                                item[previous_key] = f"{item[previous_key]},{prop}"
                    if 'id' not in item:
                        continue  # not a valid item

                    # Sanitize data
                    for k, v in item.items():
                        if k in NUMERIC_ITEM_PROPS:
                            try:
                                item[k] = int(item[k])
                            except ValueError:
                                item[k] = float(item[k])
                        elif k in STRING_ITEM_PROPS:
                            item[k] = remove_surrounding_quotes(item[k])

                    # TODO actually do something with the item
                    # print(item)

    def get_item_name_from_id(self, item_id: int, language: Optional[Language] = Language.ENGLISH_FULL):
        return self._items[item_id]
