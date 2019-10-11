#   Copyright: © 2019, Fendy Lieanata, All rights reserved.

import hashlib

# Names of files
words_file_name = "1MillionPassword.txt" #input file name
hashed_words_file_name = "1MillionPassword_hashed.txt" #output file name
# Variable
hash_type = "md5"

def create_hash_md5_text_file(input_list, output_file_name, hash_type):
	input_list = list(map(str.strip, input_list)) # strips away the \n
	hashesToExport = []

	# loop through the words in the input list
	for word in input_list:
		if hash_type == "md5":
			crypt = hashlib.md5()
		elif hash_type == "sha1":
			crypt = hashlib.sha1()
		crypt.update(bytes(word, encoding='utf-8'))
		hashOfWord = crypt.hexdigest()
		
		hashesToExport.append(hashOfWord)

	print("Creating hash text file: {} ...".format(output_file_name))

	# Creating the output file
	with open(output_file_name, 'w') as f:
	    for hashOfWord in hashesToExport:
	        f.write("%s\n" % hashOfWord)

	print("{} has been successfully created".format(output_file_name))

def get_list_of_words_from_file(filename):
	# OPENING FILE
	print("Opening file: {}".format(filename))
	list_of_words = open(filename, 'r', errors='ignore').readlines()
	print("Striping breakline characters from the file: {}.".format(filename))
	list_of_words = list(map(str.strip, list_of_words))
	return (list_of_words)

# get words from file
words_list = get_list_of_words_from_file(words_file_name)

# create the hash
create_hash_md5_text_file(words_list, hashed_words_file_name, hash_type)


