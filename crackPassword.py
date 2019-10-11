#   Copyright: © 2019, Fendy Lieanata, All rights reserved.
import time
import multiprocessing
import math

# Create a function called "chunks" with two arguments, l and n:
def chunks(LIST, NUMBER_OF_PARTS):
    # For item i in a range that is a length of l,
    for i in range(0, len(LIST), NUMBER_OF_PARTS):
        # Create an index range for l of n items:
        yield LIST[i:i+NUMBER_OF_PARTS]

hashed_password_file_name = '1MillionPassword_hashed.txt'
hashed_guess_words_file_name = 'english_hashed.txt'

no_of_cpu = multiprocessing.cpu_count()

start = time.perf_counter()

####### OPENING HASHED PASSWORD FILE #######
print("Opening file: {}".format(hashed_password_file_name))
hashed_passwords_list = open(hashed_password_file_name, 'r').readlines()
hashed_passwords_list = list(map(str.strip, hashed_passwords_list)) # strips away all of the \n
finish = time.perf_counter()

####### OPENING HASHED GUESSED WORDS FILE #######
print("Opening file: {}".format(hashed_guess_words_file_name))
hashed_words_list = open(hashed_guess_words_file_name, 'r').readlines()
hashed_words_list = list(map(str.strip, hashed_words_list)) # strips away all of the \n
finish = time.perf_counter()

####### SPLITTING HASHED PASSWORD FILE #######
print("This computer has {0} number of CPUs. Commencing splitting of password list into {0} parts".format(no_of_cpu))
no_of_elements_in_sublist = math.ceil(len(hashed_passwords_list)/no_of_cpu)
chunks_of_password_lists = list(chunks(hashed_passwords_list, no_of_elements_in_sublist))


####### START DICTIONARY ATTACK #######
print("Starting dictionary attack on the {} password lists...".format(len(chunks_of_password_lists)))

def crack(hashed_passwords_list, cpu_number):
	number_of_cracked_password = 0
	number_of_passwords_scanned = 0

	for hashed_word in hashed_words_list:
		number_of_passwords_scanned += 1
		if hashed_word in hashed_passwords_list:
			number_of_cracked_password += 1
		if number_of_passwords_scanned % 1000 == 0:
			finish = time.perf_counter()
			print("CPU {}: {}/{} password has been cracked. {} minutes elapsed.".format(cpu_number, number_of_cracked_password, len(hashed_passwords_list), round((finish-start)/60,2)))

### EXECUTING CODES WITH MULTIPLE CPUS ###
if no_of_cpu == 2:
	p1 = multiprocessing.Process(target=crack, args=[chunks_of_password_lists[0],"1"])
	p2 = multiprocessing.Process(target=crack, args=[chunks_of_password_lists[1],"2"])

	p1.start()
	p2.start()

	p1.join() # waits until the process is completed
	p2.join()
	print("Cracking has been completed")
elif no_of_cpu == 4:
	p1 = multiprocessing.Process(target=crack, args=[chunks_of_password_lists[0],"1"])
	p2 = multiprocessing.Process(target=crack, args=[chunks_of_password_lists[1],"2"])
	p3 = multiprocessing.Process(target=crack, args=[chunks_of_password_lists[2],"3"])
	p4 = multiprocessing.Process(target=crack, args=[chunks_of_password_lists[3],"4"])

	p1.start()
	p2.start()
	p3.start()
	p4.start()

	p1.join() # waits until the process is completed
	p2.join()
	p3.join()
	p4.join()
	print("Cracking has been completed")

else:
	print("Error message: You have {} CPU. This code has been constructed for either 2 or 4 CPU.".format(no_of_cpu))
	print("How to fix: Go to line 52-77. I have hardcoded the number of processors to run this. You'll just have to change the if-else statement to cater to your number of cpu.")


