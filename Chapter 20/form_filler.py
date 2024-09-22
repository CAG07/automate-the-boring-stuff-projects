#form_filler.py - Automatically fills in the Goole form

import pyautogui, time

#Form data
form_data = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
            'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
            'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
            'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
            'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
           ]

for person in form_data:

#Give the user a chance to kill the script
    print('Give the user a chance to kill the script with CTRL-C')
    time.sleep(5)

#Wait until the form page has loaded
    print('Wait until the form page has loaded')
    time.sleep(5)

#Fill out the Name Field    
    print('Fill out the Name Field')
    pyautogui.write(person['name'] + '\t')

#Fill out the Greatest Fear(s) field
    print('Fill out the Greatest Fear(s) field')
    pyautogui.write(person['fear'] + '\t')

#Fill out the Source of Wizard Powers field
    print('Fill out the Source of Wizard Powers field')
    if person['source'] == 'wand':
        pyautogui.write(['down', '\t'])
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down', '\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down', 'down', '\t'])
    elif person['source'] == 'money':
        pyautogui.write(['down', 'down', 'down', 'down', '\t'])

#Fill out the Robocop field
    print('Fill out the Robocop field')
    if person['robocop'] == 1:
        pyautogui.write([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.write(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.write(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', '\t'])

#Fill out the Additional Comments field
    print('Fill out the Additional Comments field')
    pyautogui.write(person['comments'] + '\t')

#Click Submit
    print('Click Submit')
    time.sleep(5)
    pyautogui.write(['enter'])

#Wait until form page has loaded
    print('Wait until form page has loaded')
    time.sleep(5)

#Click the Submit another response link
    print('Click the Submit another response link')
    pyautogui.write(['enter'])
    time.sleep(5)
