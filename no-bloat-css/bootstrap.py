# Find bootstrap.css

def locate_bootstrap():
	bootstrap_path = raw_input("Enter the path to bootstrap.css >>")
	return bootstrap_path

def copy_bootstrap():	
	# create a copy of bootstrap.css to edit and save the original bootstrap file.
	import os
	import shutil
	
	filename1 = locate_bootstrap()
	filename2 = 'master_bootstrap.css'

	if os.path.isfile (filename1):
		filename2_exists = os.path.isfile (filename2)
		shutil.copy (filename1, filename2)
		global master_bootstrap 
		master_bootstrap = filename2
		
		if filename2_exists == True:
			print "Succesfully updated master_bootstrap.css"
		else: 
			print "Successfully created master_bootstrap.css"
	
	else:
		print "I'm sorry, there is no file in that location. \nPlease try again."
		copy_bootstrap()
		
	
	
def find_css(type):
	global master_bootstrap
	my_file = master_bootstrap
	my_string = type
	infile = open(my_file,"r")
	numlines = 0
	found = 0
	print "The string type is", my_string
	for line in infile:
		numlines += 1

 		if my_string in line:
			found += 1
			
	if my_string == '.':
		my_string = 'CSS Classes'	
	elif my_string == '#':
			my_string = 'CSS ID\'s'
	
	print found, my_string, "were found in", numlines, "lines."
	return found, numlines

def get_css_names():

	#Create a dictionary showing each Style/ID name & how many times it appeared in file
	foundname = False
	global master_bootstrap 
	with open(master_bootstrap, 'r') as searchfile:
		for line in searchfile:
			if '.****' in line:
				found_name.append("somethingfound??")
				css_names[found_style] = ""

def find_css_class():
	find_css('.')
	
def find_css_id():
	find_css('#')
	
	
def searchable_folders():
	# searchable_folders = [folders, that, can, be, searched]
	# a checkbox option would be ideal.
	pass


copy_bootstrap()
find_css_class()
find_css_id()
