# python-yacc
This tool generates lex codes and yacc codes from language specifications written in yacc files. It also gives a file structure of a language parser.

## Two passes
For a language specification, we have lex spec and yacc spec. Both files can be written in yacc format. We can call them "yacc file for lex" and "yacc file for yacc". This program processes a yacc file, therefore, it can process both yacc file for lex and yacc file for yacc. When it processes "yacc file for lex", it generates lex code for processing
the lex of the language. When it processes "yacc file for yacc", it generates yacc code for processing the yacc of the language.

## Directory structure
* pbase, pdata - base functions and global variable used by both lex pass and yacc pass.
* plexdata, plexbase, plexbefore, plex, plexafter - lex pass of an yacc file.
* pyaccdata, pyaccbase, pyaccbefore, pyacc, pyaccafter - yacc pass of an yacc file.
* plex.txt, pyacc.txt - yacc file for lex, yacc file for yacc.

## Usage
* First you write the language specification - the lex file and yacc file for a languare. They are both in yacc format.
* Make a copy of the whole directory. Replace plex.txt and pyacc.txt with your files.
* Run pgencode.py. It gives you
- The lex codes and yacc codes for your languare.
- Undefined terms in your lex and yacc files.
* Make another copy of the whole directory. Use generated lex codes and yacc codes to replace plex.py and pyacc.py.
* You will be using prun.py to do whatever you want to do with your language. But before you do that, you need to define undefined terms in your lex file and yacc file. That is, you write functions (to define the undefined terms) in plexbefore.py and pyaccbefore.py.
* If you used unsupported format in your lex file and yacc file, you can also extend this tool. This follows a similar process, but in a more "bootstrap" manner, after all, a lex file and a yacc file are just samples of a language called "yacc".
