LUA_COMMENT_OPERATOR = '--'


def is_quoted(string: str) -> bool:
    return (string.startswith("'") and string.endswith("'")) or (string.startswith('"') and string.endswith('"'))


def remove_surrounding_quotes(string: str) -> str:
    if len(string) >= 3 and is_quoted(string):
        return string[1:-1]
    return string
