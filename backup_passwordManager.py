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
		##STILL IN PROGRESS## create a password generator if they want it generated
	# 2. find existing account password
		# ask for what site it's for/game/anything else
		# return username and password
	# 3. check how many accounts is currently stored
		# displays amount of accounts currently stored
	# 4. exit
		# terminates the program

import json
import getpass
import random

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
		temp = open('masterPass.txt', 'r')
	except FileNotFoundError:
		newUser = True
		print("File not found. Creating new user...")

	# creates a new user if one does not exist already
	if newUser:
		CreateNewUser()
	else:
		# continues to ask for masterpass from user
		while checkUser == False:
			checkUser = FindMasterPass()

	# close temp file
	temp.close()

	# opens size.txt and reads the amount of accounts there are stored
	with open('size.txt', 'r') as readSize:
				size = readSize.read()
				totalAccounts = int(size)

	# open password.txt and read dictionary and store it into passwordManager
	# use update
	if totalAccounts > 0:
		infile = open('password.txt', 'r')
		passwordManager = eval(infile.read())

	# continuous loop until user exits
	while True:
		Menu()
		userChoice = input("Pick an option: ")

		# 1. enter new account
		if userChoice == '1':

			# AddAccount adds an account to file and returns a dictionary
			account = AddAccount()
			passwordManager.update(account)
			print("Account added")
			totalAccounts += 1

		# 2. find existing account password
		elif userChoice == '2':
			FindAccount(passwordManager)

		# 3. check how many accounts is currently stored
		elif userChoice == '3':
			totalAccounts = len(passwordManager)
			print("Size: {}".format(totalAccounts))
		# 4. exit
		elif userChoice == '4':

			# push passwordManager dictionary into a text file
			# open a text file and write into it
			# will pull from that text file when program executes
			with open('password.txt', 'w') as password:
				password.write(str(passwordManager))

			# stores totalAccount size into a size.txt file
			with open('size.txt', 'w') as size:
				size.write(str(totalAccounts))
			print("Terminating program.")
			exit()
		else:
			print("Wrong choice try again..")


# Define Menu function
# -- displays a menu to output for user to choose from
# -- receives: nothing
# -- returns: nothing
def Menu():
		print('''MENU:
	1. Enter new account
	2. Find existing account
	3. Check how many accounts are currently stored
	4. Exit''')
	
# Define AddAccount function
# -- gets an account from user and returns it in a form of a dictionary
# -- receives: nothing
# -- returns: account(dictionary containing all the info)
def AddAccount():
	title = input("Enter title for account: ").lower()
	username = input("Enter username: ").lower()

	# print out 2 choices
		# 1. entered by user
		# 2. random generated password
	while True:
		print("1) Enter password manually\n" +
			  "2) Auto generate password")
		userChoice = input()

		# let user manually input their own password
		if userChoice == "1":
			password = input("Enter password: ")
			account = {title: {'username':username, 'password':password}}
			break

		# auto generates a password
		elif userChoice == "2":
			passLen = int(input("Enter password desired length: "))
			s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
			password = "".join(random.sample(s, passLen))
			account = {title: {'username':username, 'password':password}}
			break
			
		else:
			print("Wrong input.. Please try again.")	

	return account



def FindAccount(passwordManager):
	title = input("Enter title to find: ").lower()
	account = passwordManager.get(title)
	if account == None:
		print("Account does not exist.")
		return
	print("Username: " + account['username'])
	print("Password: " + account['password'])
	


# Define FindMasterPass function
# -- finds master password from text file
# -- receives: temp(open file)
# -- returns: true or false if password was correct
def FindMasterPass():
	temp = open('masterPass.txt', 'r')

	masterPass = getpass.getpass("Enter Master Password: ")
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
	outfile = open('masterPass.txt', 'w')
	outfile.write(masterPass)
	outfile.close()

	# create a password text file to hold all the passwords
	outfile = open('password.txt', 'w')
	outfile.close()

	# create a size text file to keep track of the size of the program
	with open('size.txt', 'w') as handle:
		handle.write(str(0))

	print("New user created.. Please restart program.")
	exit()


main()