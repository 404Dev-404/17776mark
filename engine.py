import export
import parser
import parser_exceptions


class Engine:
    def __init__(self, input_path: str, output_path: str, mode: str) -> None:
        self.input_path: str = input_path
        self.output_path: str = output_path
        self.mode: str = mode

        self.ps = parser.Parser()

    def compile(self) -> bool:
        with open(self.input_path, "r") as input_contents:
            try:
               self.ps.compile(input_contents.read())
            except (parser_exceptions.ParserInvalidLine,
                    parser_exceptions.ParserInvalidOptionKey,
                    parser_exceptions.ParserUndefinedCharacter,
                    parser_exceptions.ParserOptionsConflict) as err:
                print(err)
                return False
        return True

    def export(self) -> None:
        match self.mode:
            case "html":
                exporter = export.HTMLExport(self.ps.characters_defined, self.ps.dialogue, self.ps.parser_options.copy())
            case "ao3":
                exporter = export.AO3Export(self.ps.characters_defined, self.ps.dialogue, self.ps.parser_options.copy())
            case _:
                raise parser_exceptions.ParserInvalidExportMode(self.mode)

        with open(self.output_path, "w") as output_file:
            output_file.write(exporter.generate_output())
