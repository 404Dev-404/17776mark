from dataclasses import dataclass

import parse

import parser_exceptions

markup_patterns = [
    ('character', "#character {name} {colour:x} {indent:d}"),
    ('option', "#option {key} {value}"),
    ('dialogue', "{name}: \"{contents}\"")
]

default_parser_options = {
    "dialogue.initial_dots": "False",
    "dialogue.add_name_tags": "False",
    "format.indent_width": "10",
    "format.font_family": "Arial",
    "format.font_size": "1.25rem"
}

@dataclass
class CharacterDef:
    name: str
    color: int
    indent: int

@dataclass
class DialogueDef:
    name: str
    contents: str

class Parser:
    def __init__(self):
        self.characters_defined: list[CharacterDef] = []
        self.dialogue: list[DialogueDef] = []
        self.defined_character_names: list[str] = []
        self.parser_options: dict[str, str] = default_parser_options.copy()

    def compile(self, input: str) -> None:
        lines: list[str] = input.splitlines()
        #print(lines)

        for num, line in enumerate(lines):
            if line == '':
                continue

            for type, pattern in markup_patterns:
                parsed_line = parse.parse(pattern, line)
                if parsed_line is not None:
                    #print(parsed_line)
                    match type:
                        case 'character':
                            self._handle_character(parsed_line)
                        case 'option':
                            self._handle_option(parsed_line, num)
                        case 'dialogue':
                            self._handle_dialogue(parsed_line, num)
                    break
            else:
                raise parser_exceptions.ParserInvalidLine(num, line)

    def _handle_character(self, character_parse: parse.Result) -> None:
        character_definition: CharacterDef = CharacterDef(character_parse['name'], character_parse['colour'], character_parse['indent'])
        self.characters_defined.append(character_definition)
        self.defined_character_names.append(character_parse['name'])

        #print(self.characters_defined)

    def _handle_option(self, option_parse: parse.Result, line_num: int) -> None:
        #print(option_parse)

        if option_parse['key'] in self.parser_options:
            self.parser_options[option_parse['key']] = option_parse['value']
        else:
            raise parser_exceptions.ParserInvalidOptionKey(line_num, option_parse['key'])

        if self.parser_options['dialogue.initial_dots'] == "True" and self.parser_options['dialogue.add_name_tags'] == "True":
            raise parser_exceptions.ParserOptionsConflict("dialogue.initial_dots", "dialogue.add_name_tags", "Initial dots and name tags cannot be combined.")

        print(self.parser_options)

    def _handle_dialogue(self, dialogue_parse: parse.Result, line_num: int) -> None:
        name: str = dialogue_parse['name']
        contents: str = dialogue_parse['contents']

        if name not in self.defined_character_names:
            raise parser_exceptions.ParserUndefinedCharacter(line_num, name)
        else:
            if self.parser_options['dialogue.initial_dots'] == "True":
                contents = "." + contents

            if self.parser_options['dialogue.add_name_tags'] == "True":
                contents = name.upper() + ": " + contents

            line_of_dialogue: DialogueDef = DialogueDef(name, contents)
            self.dialogue.append(line_of_dialogue)
