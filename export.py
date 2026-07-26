from parser import CharacterDef, DialogueDef


class Export:
    def __init__(self, chars: list[CharacterDef], dialogue: list[DialogueDef], options: dict[str, str]):
        self.chars = chars
        self.dialogue = dialogue
        self.options = options

class HTMLExport(Export):
    def generate_output(self) -> str:
        html: str = ""

        html += "<!DOCTYPE html>"
        html += "<html>"          # starting HTML

        html += "<head>"          # starting head

        html += "<style>"         # starting style

        html += self._generate_dialogue_style()

        html += " "

        for character in self.chars:
            html += self._generate_character_style(character)

        html += "</style>"        # closing style

        html += "</head>"         # closing head

        html += "<body>"          # starting body

        for line in self.dialogue:
            html += self._generate_line_of_dialogue(line)

        html += "</body>"         # closing body

        html += "</html>"         # closing HTML

        return html

    def _generate_character_style(self, character: CharacterDef) -> str:
        name: str = character.name
        color: int = character.color
        indent: int = character.indent

        style: str = f".{name} {{color: #{color:x}; padding-left: {int(self.options['format.indent_width']) * indent}%;}}"

        return style

    def _generate_dialogue_style(self) -> str:
        style: str = f"""body {{background-color: #000000; font-family: \"{self.options['format.font_family']}\"; font-size: {self.options['format.font_size']}; line-height: 1.6;}}"""

        return style

    def _generate_line_of_dialogue(self, line: DialogueDef) -> str:
        para: str = f"<p class=\"{line.name}\">{line.contents}</p>"

        return para

class AO3Export(Export):
    def generate_output(self) -> str:
        output = ""

        output += "<!-- WORKSKIN INCLUDED HERE!!!\n"

        output += self._generate_dialogue_style()

        for char in self.chars:
            output += self._generate_character_style(char)

        output += "-->\n\n"

        output += "<div class=\"dialogue\">" #open div

        for line in self.dialogue:
            output += self._generate_line_of_dialogue(line)

        output += "</div>" #close div

        return output

    def _generate_dialogue_style(self) -> str:
        style: str = ""
        style += "#workskin dialogue {\n"
        style += "\tbackground-color: #000000;\n"
        style += f"\tfont-family: {self.options['format.font_family']};\n"
        style += f"\tfont-size: {self.options['format.font_size']};\n"
        style += "\tline-height: 1.6;\n"
        style += "}\n\n"

        return style

    def _generate_line_of_dialogue(self, line: DialogueDef) -> str:
        para: str = f"<p class=\"{line.name}\">{line.contents}</p>"

        return para

    def _generate_character_style(self, char: CharacterDef) -> str:
        style: str = ""

        style += f"#workskin {char.name} {{\n"
        style += f"\tcolor: #{char.color:x};\n"
        style += f"\tmargin-left: {char.indent * self.options['format.indent_width']}%;\n"
        style += f"}}\n\n"

        return style
