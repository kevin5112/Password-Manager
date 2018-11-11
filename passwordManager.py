# Password Manager
# can use python
# or use c++
# use dictionary?
# eventually turn it into a web app
# use text files to hold the passwords and info so that there's
# access when after program terminates and restarts

# 0. originally when ran, check to see if it's a new user or existing
	# if new, ask to choose a master password
	# if existing, ask for password.
	# story password in text file
# 1. display to ask for master password.

# 2. menu 
	# a. display options.
		# 1. enter new account
		# 2. find existing account password
		# 3. check how many accounts is currently stored
		# 4. exit

# Menu
	# 1. enter new account
		# ask for the details of account (email, username, site, game)
		# ask if wanted to generate password or input themselves
		# create a password generator if they want it generated
	# 2. find existing account password
		# ask for what site it's for/game/anything else
		# return username and password?
	# 3. check how many accounts is currently stored
		# return total accounts stored
	# 4. exit
		# terminates the program
import os
import json
import ast

# class Account:

#Define main function
def main():
	newUser = False
	passwordManager = {}
	checkUser = False
	totalAccounts = 0

	# check to see if it's a new user or existing user by checking
	# if the password file exists
	try:
		temp = open(r'/Users/kevamp/Desktop/CompSci/Project/Password_Manager/masterPass.txt', 'r')
	except FileNotFoundError:
		newUser = True
		print("File not found. Creating new user...")

	# creates a new user if one does not exist already
	if newUser:
		CreateNewUser()
	else:
		while checkUser == False:
			checkUser = FindMasterPass()

	# continuous loop until user exits
	while True:
		Menu()
		userChoice = input("Pick an option: ")

		# 1. enter new account
		if userChoice == '1':
			title = input("Enter title: ")
			passwordManager = AddAccount(title)
			print(passwordManager)
		# 2. find existing account password
		elif userChoice == '2':
			FindAccount()
		# 3. check how many accounts is currently stored
		elif userChoice == '3':
			totalAccounts = Size()
			print("Total accounts:", totalAccounts)
		# 4. exit
		elif userChoice == '4':
			temp.close()
			print("Terminating program.")
			exit()
		else:
			print("Wrong choice try again..")

	# AddPassword(passwordManager)


# Define Menu function
# -- displays a menu to output for user to choose from
# -- receives: nothing
# -- returns: nothing
def Menu():
		print('''MENU:
	1. Enter new account
	2. Fine existing account
	3. Check how many accounts are currently stored
	4. Exit''')
	
# Define AddAccount function
# -- gets an account from user and adds it to file database
# -- receives: title(string of title of the account from user)
# -- returns: account(dictionary containing all the info)
def AddAccount(title):
	username = input("Enter username: ")
	password = input("Enter password: ")
	account = {title: {'username':username, 'password':password}}

	# write account to file
	appendfile = open(r'/Users/kevamp/Desktop/CompSci/Project/Password_Manager/password.txt', 'a')
	readfile = open(r'/Users/kevamp/Desktop/CompSci/Project/Password_Manager/password.txt', 'r')

	if len(readfile.read()) == 0:
		appendfile.write(json.dumps(account))
	else:
		appendfile.write('\n' + json.dumps(account))
	appendfile.close()
	readfile.close()
	return account

# Define Size function
# -- gives the user how many accounts are currently being stored in program
# -- receives: nothing
# -- returns: Size(integer telling how many accounts are currently stored)
def Size():
	readfile = open(r'/Users/kevamp/Desktop/CompSci/Project/Password_Manager/password.txt', 'r')
	allAccounts = {}
	while readfile.readline() != '':
		d = readfile.readline()
		d = d.rstrip('\n')
		d = ast.literal_eval(d)
		title = d.keys()
		allAccounts[title] = d[title]
	#size = len(allAccounts)
	print(allAccounts)
	#return size



# Define FindMasterPass function
# -- finds master password from text file
# -- receives: temp(open file)
# -- returns: true or false if password was correct
def FindMasterPass():
	temp = open(r'/Users/kevamp/Desktop/CompSci/Project/Password_Manager/masterPass.txt', 'r')

	masterPass = input("Enter Master Password: ")
	checkString = temp.readline()

	# print("user:", masterPass)
	# print("master:", checkString)

	if masterPass == checkString:
		print("Unlocked.")
		return True
	else:
		print("Invalid password.")
		return False

	temp.close()


# Define CreateNewUser function
# -- creates a new user and makes a new text files to write password to
# -- as well as asks for a master password
# -- receives: nothing
# -- returns: nothing
def CreateNewUser():
	# ask user for master password
	masterPass = input("Enter master password(Very important. Do not forget this password): ")
	
	# create master password file to hold the one password
	outfile = open(r'/Users/kevamp/Desktop/CompSci/Project/Password_Manager/masterPass.txt', 'w')
	outfile.write(masterPass)
	outfile.close()

	# create a password text file to hold all the passwords
	outfile = open(r'/Users/kevamp/Desktop/CompSci/Project/Password_Manager/password.txt', 'w')
	outfile.close()

	print("New user created.. Please restart program.")
	exit()


# Define AddPassword function
# -- Adds an account to the password.txt file using a dictionary
# -- receives: passwordManager dictionary
# -- return: true or false if add was completed
def AddPassword(passwordList):
	addResult = True
	key = "tinky\n"
	username = "tinky\n"
	password = "pie\n"
	website = "tinkypie.com\n"

	passwordList[key] = (username, password, website)
	AddToFile(passwordList, key)


def AddToFile(list, key):
	outfile = open(r'/Users/kevamp/Desktop/CompSci/Project/Password_Manager/password.txt', 'a')
	for i in range(3):
		print("poop")
		outfile.write(list[key][i])	
	outfile.close()


main()