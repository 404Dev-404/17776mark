#!/usr/bin/python

import argparse
from pathlib import Path
import sys

import engine
import parser_exceptions

def main() -> None:
    argparser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog='17776mark',
        description='Markup language for 17776-style dialogue'
    )

    argparser.add_argument("input", type=str, help="The path for the markup input.")
    argparser.add_argument("-o", "--output", type=str, help="A specific path for the HTML output. If no path is provided, the HTML output will have the same filename as the markup.")
    argparser.add_argument("-m", "--mode", type=str, help="The output mode for 17776mark. Currently, these options are \"html\" and \"ao3\".")

    args: argparse.Namespace = argparser.parse_args()

    input_path = args.input

    if args.output == None:
        out_path = Path(args.input).stem + ".html"
    else:
        out_path = args.output

    if args.mode == None:
        export_mode = "html"
    else:
        export_mode = args.mode

    try:
        e = engine.Engine(input_path, out_path, export_mode)
    except parser_exceptions.ParserInvalidExportMode as err:
        print(err)
        sys.exit()

    result = e.compile()

    if result:
        print(f"17776mark: Successful compilation of {args.input}!")
    else:
        print(f"17776mark: Failed to compile {args.input}.")

    e.export()


if __name__ == "__main__":
    main()
