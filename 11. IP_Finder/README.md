# IP Address Finder in Python

### This is small (but fun) program that I made in python
### You can find your Hostname, local IP and Public IP With this program

## Modules Used
- socket
- requests

socket is a standard module that comes with python, whereas requests needs to be installed

## Steps to use this keylogger
- Type this command in terminal if you have git installed 
  ```git clone https://github.com/IAmMaulik/IP_Finder.git```
- Type this command in your terminal
	```pip install -r requirements.txt```
- Run the program by writing ```./main.py```


## Point to note
- Gor Hostname, I have used socket's gethostname() function
- For Local IP, I have used socket's gethostbyname() function
- For Public IP. I have used the requests module to get respose from the api of ipify.org

# Thanks for reading through
