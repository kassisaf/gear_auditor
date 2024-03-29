import os.path
import re

CONTAINER_PATTERN = re.compile(r'\["([\w\d ]+)"] = {')
ITEM_PATTERN = re.compile(r'^\s*\["([\w\d ]+)"] = (\d+),?[\r\n\s]*$')


class FindAllLuaFile:
    def __init__(self, file_path: str):
        self._file_path = file_path
        self._filename = os.path.split(file_path)[-1]
        self._character_name = os.path.splitext(self._filename)[0]
        self._gil = -1
        self._items = {}

        self._parse()

    def __str__(self):
        return f"{self._filename} {self.__class__}"

    def _parse(self):
        with open(self._file_path, 'r', encoding='utf8') as file:
            current_container = None
            for line in file:
                container_match = CONTAINER_PATTERN.match(line)
                if container_match:
                    current_container = container_match.group(1)
                    self._items[current_container] = {}
                    continue
                item_match = ITEM_PATTERN.match(line)
                if item_match:
                    item_id = item_match.group(1)
                    quantity = int(item_match.group(2))
                    if item_id == 'gil':
                        self._gil = quantity
                        continue

                    item_id = int(item_id)
                    if item_id not in self._items[current_container]:
                        self._items[current_container][item_id] = quantity
                    else:
                        self._items[current_container][item_id] += quantity
        # print(self._items)

    def get_character_name(self):
        return self._character_name

    def get_gil(self):
        return self._gil

    def get_items(self):
        return self._items
