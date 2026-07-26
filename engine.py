import parser
import parser_exceptions


class Engine:
    ps = parser.Parser()

    def __init__(self) -> None:
        pass

    def load(self, input_path: str, output_path: str) -> None:
        self.input_path: str = input_path
        self.output_path: str = output_path

    def process(self) -> bool:
        with open(self.input_path, "r", encoding="utf-8") as input_contents:
            try:
               html_output = self.ps.process(input_contents.read())
            except (parser_exceptions.ParserInvalidLine,
                    parser_exceptions.ParserInvalidOptionKey,
                    parser_exceptions.ParserUndefinedCharacter,
                    parser_exceptions.ParserOptionsConflict) as err:
                print(err)
                return False

            #print(html_output)

            with open(self.output_path, "w", encoding="utf-8") as output_file:
                output_file.write(html_output)

        return True
