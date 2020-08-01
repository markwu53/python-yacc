# python-yacc
python yacc model, base and code generation

## Two passes
For a language specification, we have lex spec and yacc spec. Both files are in yacc format. We can call them "yacc file for lex" and "yacc file for yacc".
This program processes a yacc file, therefore, it can process both yacc files. When it processes "yacc file for lex", it generates lex code for processing
the lex of the language. When it processes "yacc file for yacc", it generates yacc code for processing the yacc of the language.

Internally, the program has a lex pass and yacc pass to process any yacc file.

## Directory structure
* pbase, pdata - base functions and global variable used by both lex pass and yacc pass.
* plbase, pldata, plmanual, plgencode, plex - lex pass of an yacc file.
* ppbase, ppdata, ppmanual, ppgencode, pyacc - yacc pass of an yacc file.
* plex.txt, pyacc.txt - yacc file for lex, yacc file for yacc.

## Usage
* It uses a "bootstrap" manner to process a new language specification.
* Make *two copies* of the whole directory - call them "bootstrap copy" and "working copy".
* Replace plex.txt and pyacc.txt with the new language specification files.
* In the bootstrap copy, run the program. The program generates (transaltes) code for lex and yacc for the new language. It also reports undefined "terms" in the lex and yacc files.
* In the working copy, use the generated code to replace plgencode.py and ppgencode.py. Define (write functions) the undefined terms in plmanual.py and ppmanual.py. Then try to run the program in the working copy.
* When make any change to the new language specification, go back to the bootstrap copy to re-generate the code, because at this time the program in the working copy usually does not work. Iterate between this step and the previous step.
* The working copy will converge to a program that can process the new language. 
