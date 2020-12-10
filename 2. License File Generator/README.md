## About
licenseFileGenerator (or LFG) is a python script which generates a LICENSE file in a user-specified local repository so the user doesn't have to do so on Github's website.  The user uses the terminal to enter which open source license they would like to use and a path in which to create the file.  It then creates the file and names it "LICENSE" so Github automatically recognizes it as such.

This program uses the LFG_Licenses repo (found here: https://github.com/Lich42/LFG_Licenses) to copy the text for each license.  Because of this, you must be connected to the internet for this program to work properly.

## Usage

1. Navigate to the folder you saved the script to and type "python3 lfg.py" into the terminal.
2. Type the command for the license you wish to use (a list of commands can be found by typing "LIST")
3. Type the path to the desired local repository when prompted.  This must be the full path, e.g. /home/YOUR_USERNAME/Desktop/Test_Repo
4. That's it, you're done!


## To-Do

This is a list of things that need working on.

1. Add more licenses.  The more the better.
2. Improve efficiency in any way possible.
