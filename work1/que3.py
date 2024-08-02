#Que 3) Write a program to add two lists index-wise. Create a new list that contains
#       the 0th index item from both the list, then the 1st index item, and so on till
#       the last element. any leftover items will get added at the end of new





list1 = ["M", "na", "i", "Ge"]
list2 = ["y", "me", "s", "et"]
max_length = max(len(list1), len(list2))
    
R = []
    
for i in range(max_length):
    concatenated = ""
        
    if i < len(list1):
        concatenated += list1[i]
        
    if i < len(list2):
        concatenated += list2[i]
        
    R.append(concatenated)
    
print(R)


#------------------------------------------------------------------------------

#OUTPUT

# ['My', 'name', 'is', 'Geet']
