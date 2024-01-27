import os


class FindAllLuaFile:
    def __init__(self, file_path: str):
        self._file_path = file_path
        self._filename = os.path.split(file_path)[-1]
        self._character_name = os.path.splitext(self._filename[0])

    # TODO: parse out item ids and locations
    # example format:

    """
    return {
    ["gil"] = 49410766,
    ["slip 24"] = {
      },
    ["slip 08"] = {
      ["11708"] = 1,
      ["12103"] = 1,
      ["12025"] = 1,
      ["11709"] = 1,
      ["19255"] = 1,
      ["11721"] = 1,
      ["12096"] = 1,
      ["16208"] = 1,
      ["11719"] = 1,
      ["11718"] = 1,
      ["11750"] = 1,
      ["12105"] = 1,
      ["12016"] = 1,
      ["11710"] = 1,
      ["11715"] = 1,
      ["11714"] = 1,
      ["11706"] = 1,
      ["16204"] = 1,
      ["11705"] = 1,
      ["11703"] = 1,
      ["12095"] = 1,
      ["11617"] = 1,
      ["19253"] = 1,
      ["12085"] = 1,
      ["19260"] = 1,
      ["16209"] = 1,
      ["16203"] = 1,
      ["19254"] = 1,
      ["12045"] = 1,
      },
    ["slip 12"] = {
      },
    ["key items"] = {
    ...
    """