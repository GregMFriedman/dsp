# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > Here are some of the commands that I most anticpate using:

```
mkdir 		make directory
		   -p	 create intermediate directories as necessary

rmdir 		remove directory
		   -p    delete intermediate directories (so be careful!)


cp 		copy a file or directory
		   Syntax is 'cp (source) (target)'
		   -i    prompt before overwriting
		   -n 	 do not overwrite
		   -R	 allows copying of directories (and their contents)

mv 		move or rename a file or directory
		   Syntax for renaming is 'mv (old name) (new name)'
		   Syntax for moving is 'mv (name) (target directory)'
		   -i	 prompt before overwriting
		   -n 	 do not overwrite

find		find files
		   (One) syntax is 'find STARTDIR -name WILDCARD -print'
		   (General) syntax is 'find [options] PATH (expr)'
		   	     where expr is made up of primaries/operands 
		   Options:
		   -d	 depth-first traversal
		   -s	 alphabetical order traversal
		   Primaries:
		   -delete	      delete found files and directories
		   		      (depth first)
		   -empty     	      return true if file or directory is empty
		   -exec and -execdir (these seem v. useful and return true 
		   	     	      contingent on a separate utility command,
				      run from pwd or from directory of the
				      current file, resp.)
		   -iname (str)	      case insensitive name search
		   -maxdepth (num)    descend at most (num) levels from PATH
		   -mindepth (num)    only test once (num) levels from PATH
		   -name (str)	      name search (use wildcards!)
		   -newer (file)      true if current file has more recent
		   	  	      modification time than (file)
		   -path (str)	      path search (use wildcards!)
		   -print	      (default) prints pathname of current file
		   -size (n)	      true if file's size (in 512-byte blocks)
		   	 	      is (n) and also can take other units
				      [ckMGTP]
		   Operators:
		   ! or -not		not
		   -false		false
		   -true		true
		   (exp) -and (exp)	logical AND (alternatively (exp)(exp))
		   (exp) -or (exp)	logical OR

grep		find things inside files
		   Syntax is 'grep (options) (pattern) (file)'
		   -c	     print a count of number of lines
		   	     containing (pattern)
		   -i 	     case insensitive matching
		   -m (num)  stop reading file after (num) matches
		   -n 	     include line numbers with matched output
		   -o	     prints only matching part of lines
		   -r 	     recursive search through subdirectories
		   -v	     inverted search (think !grep)

exit		exit the shell


cmd1|cmd2    Take the output from cmd1, pipe it as input to cmd2.


cmd<file     Take the contents of file as input for cmd.


cmd>file     Take the output from cmd and write to file.


cmd>>file    Take the output from cmd and append to file.    


man    		 Gives you information about what each command does


```
---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > The `ls` command lists all the files and folders in your current directory.  Below are some of the flags that go with it:

```

ls 		list directory
		   -l	 long output
		   -a    lists all entries
		   -A	 list all entries but . and ..
		   -lh	 display sizes in unit prefixes (B, KB, MB, ...)
		   -m	 stream output (comma separated)
		   -p	 distinguish directories by appending '/'
		   -R	 show full tree beneath pwd
		  - Glp  prints files and directories in different colors


```

>>The `ls -a` command is useful for finding your hidden files (such as .bash)

>>The `ls -l` command includes permissions, number of bytes, owner name, group, name exact time of last modification & path name. 

>> The `ls -lh` command is the same as the `ls -l` but it uses appropriate units for file sizes.  That is what happens when one combines h with any command that displays file sizes.  If there are no units to change, adding h to the end of the flag won't do anything.

>>Using all three together `ls -alh` would show all files and display all the long information in appropriate units.

---

What does `xargs` do? Give an example of how to use it.

> > I'm not sure I understand all the capacities of the `xargs` command, but the use that seems to be the most prevalent involves connecting the `find` or `grep` command with another action, such as deleting.  So essentially it allows you the ability to find and delete, like in the example below:

```
$ ls
one.c  one.h  two.c  two.h

$ find . -name "*.c" | xargs rm -rf

$ ls
one.h  two.h

```

---

