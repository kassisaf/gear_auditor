from enum import Enum
from typing import List


class ItemNameKey(Enum):
    ENGLISH = 'english',
    ENGLISH_FULL = 'english_full',
    JAPANESE = 'japanese',
    JAPANESE_FULL = 'japanese_full'


class Item:
    def __init__(
            self,
            id: int,
            en: str,
            enl: str,
            ja: str,
            jal: str,
            category: str,
    ):
        self._id = id
        self._category = category
        self._names = {
            ItemNameKey.ENGLISH: en,
            ItemNameKey.ENGLISH_FULL: enl,
            ItemNameKey.JAPANESE: ja,
            ItemNameKey.JAPANESE_FULL: jal
        }

    def __str__(self):
        return self._names[ItemNameKey.ENGLISH_FULL]

    def __eq__(self, other):
        return self._id == other.get_id()

    def get_id(self) -> int:
        return self._id

    def get_category(self) -> str:
        return self._category

    def name_matches(self, item_name: str):
        matches = (
            item_name.lower() == self._names[ItemNameKey.ENGLISH].lower()
            or item_name.lower() == self._names[ItemNameKey.ENGLISH_FULL].lower()
            or item_name == self._names[ItemNameKey.JAPANESE]
            or item_name == self._names[ItemNameKey.JAPANESE_FULL]
        )
        return matches


class GearList:
    _GEAR_CATEGORIES = ['weapon', 'armor']

    def __init__(
            self,
            job: str,  # TODO: Jobs enum populated from Windower resources?
            items: List[Item]
    ):
        self._job = job
        self._items = {}
        for item in items:
            self.add_item(item)

    def add_item(self, item: Item):
        if item.get_category().lower() in self._GEAR_CATEGORIES:
            self._items.setdefault(__key=item.get_id(), __default=item)


class Character:
    def __init__(
            self,
            name: str,
            jobs: List[GearList]
    ):
        ...