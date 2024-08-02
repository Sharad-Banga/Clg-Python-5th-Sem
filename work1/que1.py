

# Que 1 )   Write a python program to get a single string from two given strings,
#           separated by a space and swap the first two characters of each string.


str1 = 'computer'
str2 = 'Science'
new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]
    
result = new_str1 + " " + new_str2
print(result)




    
#            OUTPUT


#       Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
#       Type "help", "copyright", "credits" or "license()" for more information.

#       =========================== RESTART: D:/work1/que1.py ==========================
#       Scmputer coience
