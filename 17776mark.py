#!/usr/bin/python

import argparse
from pathlib import Path

import engine

e = engine.Engine()

def main() -> None:
    argparser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog='17776mark',
        description='Markup language for 17776-style dialogue'
    )

    argparser.add_argument("input", type=str, help="The path for the markup input.")
    argparser.add_argument("-o", "--output", type=str, help="A specific path for the HTML output. If no path is provided, the HTML output will have the same filename as the markup.")

    args: argparse.Namespace = argparser.parse_args()

    #print(args.input)
    #print(args.output)

    if args.output == None:
        e.load(args.input, Path(args.input).stem + ".html")
    else:
        e.load(args.input, args.output)

    result = e.process()

    if result:
        print(f"17776mark: Successful compilation of {args.input}!")
    else:
        print(f"17776mark: Failed to compile {args.input}.")

if __name__ == "__main__":
    main()
