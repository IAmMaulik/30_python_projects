import os
import requests

while True:
	liceName = input('(You can type "list" for a list of the available commands or "exit" to exit)\n===============\nWhich license would you like to use?: ')
	liceName = liceName.lower() #Makes the input lowercase

	if liceName == "list": 
		#Lists all the licenses and available and their commands
		#NOTE: The only reason I've used multiple "prints" is to keep the source code looking neat
		print("\n-------------\n  LICENSES\n-------------\n")
		print("LICENSE                    COMMAND\n")
		print("General Public License v3 = 'gpl'\nApache License = 'al'\nBSD 2 = 'bsd2'\nBSD 3 = 'bsd3'\nMIT = 'mit'\nUnlicense = 'ul'\nMozilla Public License v2 = 'mpl'")
		print("Affero General Public License = 'agpl'\nLesser General Public License v3 = 'lgpl'\nEclipse Public License = 'epl'\n")

		continue

	#This elif statement is split into 2 different lines to keep it from being one super long line of code
	elif liceName == 'gpl' or liceName == 'al' or liceName == 'bsd2' or liceName == 'bsd3' or liceName == 'ul' or liceName == 'mit' \
	or liceName == 'mpl' or liceName == 'agpl' or liceName == 'lgpl' or liceName == 'epl':
		repoPath = input('Please type the path to the repository: ')

		liceFile = 'https://raw.githubusercontent.com/Lich42/LFG_Licenses/master/' + liceName + '.txt' #Gets the user's desired license
		data = requests.get(liceFile)

		os.chdir(repoPath) #Changes the directory to the user's specified one

		with open("LICENSE", "w+") as text_file: 
			text_file.write(data.text) 
	
		print("Success!") 
		break

	elif liceName == "exit":
		break

	else:
		print("\nTHAT IS NOT A VALID COMMAND, PLEASE TRY AGAIN\n")
		continue
