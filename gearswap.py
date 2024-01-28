import os.path
import re
from helpers import LUA_COMMENT_OPERATOR, is_quoted, remove_surrounding_quotes

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
AUGMENTED_ITEM_PATTERN = r'{\s*(name)=\s*"(.+)",\s*augments\s*='
GEAR_SLOT_PATTERN = f"({'|'.join([f'({slot})' for slot in EQUIPMENT_SLOTS])})" + r"\s*=\s*"


class GearSwapLuaFile:
    def __init__(self, file_path: str):
        self._file_path = file_path
        self._filename = os.path.split(file_path)[-1]
        self._character_name = None
        self._job = None
        self._equipment_names = []
        self._equipment_variables = []

        self._parse_name_and_job()
        self._parse_equipment_and_variables()

    def __str__(self):
        return f"{self._filename} [{len(self._equipment_names)}n/{len(self._equipment_variables)}v] {self.__class__}"

    def get_character(self):
        return self._character_name

    def get_job(self):
        return self.job

    def get_equipment(self):
        return self._equipment_names

    def get_variables(self):
        return self._equipment_variables

    def _parse_name_and_job(self):
        filename_split_by_underscore = self._filename.split('_')
        if len(filename_split_by_underscore) == 2:
            job_maybe, file_ext = os.path.splitext(filename_split_by_underscore[1])
            if len(job_maybe) == 3 and job_maybe.isupper():
                self.name = filename_split_by_underscore[0]
                self.job = job_maybe

    def _parse_equipment_and_variables(self):
        with open(self._file_path, 'r', encoding='utf8') as file:
            for line in file:
                if line.strip().startswith(LUA_COMMENT_OPERATOR):
                    continue

                if re.search(GEAR_SLOT_PATTERN, line):
                    terms = [term.strip().replace(',', '') for term in line.split('=')]
                    if len(terms) >= 2 and terms[1] != EMPTY_SLOT:
                        terms[1] = terms[1].split(LUA_COMMENT_OPERATOR)[0].strip()  # remove trailing comments
                        if is_quoted(terms[1]):
                            unquoted = remove_surrounding_quotes(terms[1])
                            if len(terms[1]) > len(unquoted):
                                self._equipment_names.append(unquoted)
                        else:
                            # TODO: Attempt to look up variable's item name
                            # if re.search(AUGMENTED_ITEM_PATTERN, line):
                            self._equipment_variables.append(terms[1])
        self._equipment_names = list(set(self._equipment_names))
        self._equipment_variables = list(set(self._equipment_variables))
