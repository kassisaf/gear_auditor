import os.path
import re

from modules.helpers import LUA_COMMENT_OPERATOR, is_quoted, remove_surrounding_quotes
from modules.windower import Language

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
    'ear1',
    'ear2',
    'left_ring',
    'right_ring',
    'ring1',
    'ring2',
    'back',
    'neck',
    'waist',
]
AUGMENTED_ITEM_PATTERN = re.compile(r'(\S+) *= *{\s*name *=(.+),\s*augments *= *{')
GEAR_SLOT_PATTERN = re.compile(f"({'|'.join([f'(?:{slot})' for slot in EQUIPMENT_SLOTS])})" + r" *= *([^,\r\n]{4,}),?")
JOB_ABBREVIATION_PATTERN = re.compile(r'^[A-Za-z]{3}$')


class GearSwapLuaFile:
    def __init__(self, file_path: str):
        self._file_path = file_path
        self._filename = os.path.split(file_path)[-1]
        self._character_name = None
        self._job = None
        self._equipment_names = []

        self._parse_name_and_job()
        self._parse_equipment_and_variables()

    def __str__(self):
        return f"{self._filename} [{len(self._equipment_names)}] {self.__class__}"

    def get_character(self):
        return self._character_name

    def get_job(self):
        return self._job

    def get_equipment(self):
        return self._equipment_names

    def applies_to_character(self, character_name: str):
        try:
            return self._character_name.lower() == character_name.lower()
        except AttributeError:  # occurs when a character name could not be parsed from the filename (will be None)
            filename_without_extension = os.path.splitext(self._filename)[0]
            return JOB_ABBREVIATION_PATTERN.match(filename_without_extension)

    def contains_item(self, item_dict: dict) -> bool:
        for language in Language:
            if item_dict[language.value[0]].lower() in self._equipment_names:
                return True
        return False

    def _parse_name_and_job(self):
        filename_split_by_underscore = self._filename.split('_')
        if len(filename_split_by_underscore) == 2:
            job_maybe, file_ext = os.path.splitext(filename_split_by_underscore[1])
            if len(job_maybe) == 3 and job_maybe.isupper():
                self._character_name = filename_split_by_underscore[0]
                self._job = job_maybe

    def _parse_equipment_and_variables(self):
        with open(self._file_path, 'r', encoding='utf8') as file:
            for line in file:
                line = line.strip()
                # Ignore comments
                if line.startswith(LUA_COMMENT_OPERATOR):
                    continue

                # Handle lines following the pattern: slot = item
                gear_slot_search = GEAR_SLOT_PATTERN.search(line)
                if gear_slot_search is not None:
                    slot, item_name = gear_slot_search.groups()
                    if item_name == EMPTY_SLOT:
                        continue
                    self._add_equipment(item_name)
                    continue

                # Handle lines defining an augmented item
                augmented_item_search = AUGMENTED_ITEM_PATTERN.search(line)
                if augmented_item_search is not None:
                    item_variable, item_name = augmented_item_search.groups()
                    print(f'found augmented item: {item_variable} = {item_name}')
                    self._add_equipment(item_name)
                    continue

        self._equipment_names = list(set(self._equipment_names))

    def _add_equipment(self, item_name: str):
        unquoted_item_name = remove_surrounding_quotes(item_name)
        self._equipment_names.append(unquoted_item_name.lower())
