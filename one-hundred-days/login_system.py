#Day 70 Challenge
#Login System

import os

print("🌟Login System🌟")

username = os.environ['username']
password = os.environ['password']

admin_username = os.environ['admin_username']
admin_password = os.environ['admin_password']

user_name = input("Username > ")
user_pass = input("Password > ")

if user_name == username and user_pass == password:
  print("Hello normie")

elif user_name == admin_username and user_pass == admin_password:
  print("Hello admin")

else:
  print("Please try again")
