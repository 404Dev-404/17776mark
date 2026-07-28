# 17776mark
17776mark is a markup language that allows the creation of 17776-style dialogue. This software is mainly intended for fanfic writers, so the following instructions are written to try to make the process as easy to understand.

## Installation

### Windows
The simplest option is to go to releases and download the .exe of it.

### MacOS, Linux, or people who want to run from source
This program depends on Python being installed on your computer. This can be done through the [website](https://www.python.org/downloads/), or for the Linux inclined, through your package manager.

Once you have Python installed, download this repository, extract the contents (it usually downloads as a ZIP file), and in your terminal (on MacOS this is usually referred to as Terminal), type in these commands:
```
cd [the path to the repository]
pip install -r requirements.txt
```

## Usage

### Syntax

**Note:** This is a quick overview of the syntax. In vivo examples can be seen in the examples folder.

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

#### Windows
This utility is run through the command line. On your computer, this will be called Command Prompt, and can be accessed by going into the Start Menu, navigating down to the Windows System folder, and clicking on Command Prompt.

You can build dialogue by running this command.
`17776mark.exe filename.17776mk`

This compiles your 17776mk dialogue into an HTML file with the same name as your dialogue file.

To output the dialogue to another file, you can use the `-o`/`--output` flags to specify which file to output to.
`17776mark.exe filename.17776mk --output other.html`

If you want to output in AO3 mode, you can use the `-m`/`--mode` flags to set AO3 mode.
`17776mark.exe filename.17776mk --mode ao3`

**Note:** It is **necessary** that you type `ao3` as is, otherwise the program won't recognize what mode you're referring to.
**Note:** In AO3 mode, the workskin will be included at the top of the HTML in a comment titled `WORKSKIN INCLUDED HERE!`.

#### MacOS, Linux, or people who want to run from source

The process is the same, although you will be using your operating system's terminal, and instead of `17776mark.exe`, it will be `python 17776mark.py`.

## Contribution

Pull requests are welcome, but major changes will have to be discussed with me.

## Troubleshooting

Feel free to create an issue on this repository if you need assistance! Please be clear as to what exactly the issue is ahead of time, though.
