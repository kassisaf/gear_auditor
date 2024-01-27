import os
from enum import Enum
from typing import Optional


class Language(Enum):
    ENGLISH = 'en',
    ENGLISH_FULL = 'enl',
    JAPANESE = 'jal',


class WindowerResources:
    def __init__(self, windower_path: str):
        self._path = windower_path
        self._items = {}

        self.parse_items_resource_file()

    def parse_items_resource_file(self):
        items_lua = os.path.join(self._path, 'res', 'items.lua')
        ...

    def get_item_name_from_id(self, item_id: int, language: Optional[Language] = Language.ENGLISH_FULL):
        return self._items[item_id]
