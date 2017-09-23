
import sys


class Parser:

  	def reference(self, inp):
   		if inp == "0":
      			print "List of Commands:\n -h\n -p\n nano\n"
    		elif inp == "-p":
			print "prints a pyramid with as many layers as an inputted number (use: pyra -p <layers>)"
		elif inp == "nano":
			print "A terminal text editor (you can't use nano now)"
		elif inp == "-h":
			print "Reference (for a list of commands use: pyra -h\n for a description of a command use: pyra -h [command] wait how did you get here if you didn't know this, wait why would you type -h -h?)"
		else:
		    print "Error: Wrong arguments arguments, use: pyra -h for help"

	def pyramids(self, inp):
		lay = (int)(inp)

		for i in range(1, lay+1):
	
			for j in range(0,lay-i):
		
				sys.stdout.write(" ")
	
			for k in range(0, 2*i - 1):
		
				if ((k % 2) == 0):	
			
					sys.stdout.write("*")
		
				else:
			
					sys.stdout.write(" ")
	
			sys.stdout.write("\n")
x = Parser()
p = sys.argv
if len(p) > 1:
	if p[1] == "-h":
		if len(p) == 3:
			x.reference(p[2])
		elif len(p) == 2:
			x.reference("0")
		else:
			print("Error: Wrong arguments arguments, use: pyra -h for help")
	elif p[1] == "-p":
		if len(p) == 3:
			x.pyramids(p[2])
		else:
			print("Error: Wrong arguments arguments, use: pyra -h for help")
	else:
		print("Error: Wrong arguments arguments, use: pyra -h for help")
else:
	print("Error: too few arguments, use: pyra -h for help")