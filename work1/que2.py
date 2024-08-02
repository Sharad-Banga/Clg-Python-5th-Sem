#Que 2)     Write a Python program to add 'ing' at the end of a given string (length
#             should be at least 3). If the given string already ends with 'ian', add 'ly'
#           instead. If the string length of the given string is less than 3, leave it
#           unchanged.


#----------------------------------------------------------------------------------


string = 'CSE'


if len(string) >= 3:
    if string.endswith('ian'):
        result = string + 'ly'
    else:
        result = string + 'ing'

print(result)


#----------------------------------------------------------------------------------

#OUTPUT 


#Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.

#= RESTART: D:/work1/que2.py


#CSEing
