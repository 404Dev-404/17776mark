# 17776mark
17776mark is a markup language that allows the creation of 17776-style dialogue.

## Installation
This program depends on Python being installed on your computer.
No installation is required. Everything is self-contained.

## Usage

### Syntax

**Note:** This is a quick overview of the syntax. Extended information is included in the manual.

**Note:** The names of arguments are written in brackets. When writing in said arguments, leave out the brackets.

It is recommended to use the extension `.17776mk`, but the program will accept any extension.

There are two kinds of processor directives, `#character` and `#option`

The `#character` directive allows you to define a character by name, with a colour (as a hex code, no hashtag), and a level of indentation (as multiples of the left margin of each line of dialogue).

The syntax for this directive is as follows:
```
#character [name] [colour] [indent]
```

The `#option` directive allows you to set options for the dialogue's formatting through its corresponding key.

The syntax for this directive is as follows:
```
#option [key] [value]
```

For lines of dialogue, write it in transcript form; as follows: 
```
[character]: "[text]"
```

### Building Dialogue
This application is operated through the command line. In the future, a GUI *could* be implemented, but it's up in the air.

```
python 17776mark.py filename.17776mk
```
This compiles your 17776mk dialogue into an HTML file with the same name as your dialogue file.

To output the dialogue to another file you can use the `-o`/`--output` flags
```
python 17776mark.py filename.17776mk -o other.html
```
