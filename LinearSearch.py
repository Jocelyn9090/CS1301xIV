
#Write a function called linear() that takes two parameters
#- a list of strings and a string. Write this function so
#that it returns the first index at which the string is
#found within the list if the string is found, or False if
#it is not found. You do not need to worry about searching
#for the search string inside the individual strings within
#the list: for example, linear(["bobby", "fred"], "bob")
#should return False, but linear(["bob", "fred"], "bob")
#should return 0.
#
#Use a linear search algorithm (not as scary as it sounds).
#Do not use the list method index -- in this exercise,
#you're actually implementing the way the index method
#works!


#Write your code here!
def linear(list_of_strings, astring):
    if astring not in list_of_strings:
        return False
    else:
        i = 0
        while i <= len(list_of_strings) - 1:
            if list_of_strings[i] == astring:
                return i
            else:
                i += 1

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: 3
a_list = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
print(linear(a_list, 6))
print(linear(["bobby", "fred"], "bob"))
print(linear(["bob", "fred"], "bob"))


## sample

#First, we declare the function:
def linear(a_list, an_item):
    
    #Then, we iterate through the list:
    for i in range(len(a_list)):
        
        #If we've found the item, we're done! Go ahead and
        #return this index.
        if a_list[i] == an_item:
            return i
        
    #If we reach the end of the function it means we never
    #returned an index, which means we never found the item
    #and can return False.
    return False



a_list = [5, 1, 3, 6, 7, 3, 1, 6, 7, 8, 3, 6]
print(linear(a_list, 6))

