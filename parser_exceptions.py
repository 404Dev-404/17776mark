class ParserInvalidLine(Exception):
    def __init__(self, line_num: int, line_content: str):
        super().__init__()
        self.line_num = line_num
        self.line_content = line_content

    def __str__(self):
        return f"17776mark: Invalid markup at line {self.line_num + 1}: (\"{self.line_content}\")"

class ParserInvalidOptionKey(Exception):
    def __init__(self, line_num: int, option_key: str):
        super().__init__()
        self.line_num = line_num
        self.option_key = option_key

    def __str__(self):
        return f"17776mark: Invalid option key at line {self.line_num}: ({self.option_key})"

class ParserUndefinedCharacter(Exception):
    def __init__(self, line_num: int, character_name: str):
        super().__init__()
        self.line_num = line_num
        self.character_name = character_name

    def __str__(self):
        return f"17776mark: Undefined character '{self.character_name}' at line {self.line_num}."

class ParserOptionsConflict(Exception):
    def __init__(self, option_a: str, option_b: str, conflict: str):
        super().__init__()
        self.option_a = option_a
        self.option_b = option_b
        self.conflict = conflict

    def __str__(self):
        return f"17776mark: Conflict in options \"{self.option_a}\" and \"{self.option_b}\". ({self.conflict})."
