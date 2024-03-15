#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard. 
#Check pyperclip repo for compatibility with recent versions of Python

import webbrowser, sys
webbrowser.open('https://inventwithpython.com/')

#Get a street address from the command line arguments or clipboard
#if len(sys.argv) > 1:
    #Get address from command line.
    #address = ' '.join(sys.argv[1:])

#else:
    #Get address from clipboard.
    #address = pyperclip.paste()

#webbrowser.open('https://www.google.com/maps/place/' + address)
