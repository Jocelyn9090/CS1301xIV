#We've written the function, sort_with_bubbles, below. It takes
#in one list parameter, lst. However, there are two problems in
#our current code:
# - There's a missing line
# - There's a semantic error (the code does not raise an
#   error message, but it does not perform correctly)
#
#Find and fix these problems! Note that you should only need
#to change or add code where explicitly indicated.
#
#Hint: If you're stuck, use an example input list and trace
#the code and how it modifies your list on paper. For
#example, try writing out what happens to the following list:
#
#  [34, 16, 2, 78, 4, 6, 1]

def sort_with_bubbles(lst):
    #Set swap_occurred to True to guarantee the loop runs once
    swap_occurred = True
    
    #Run the loop as long as a swap occurred the previous time
    while swap_occurred:
        
        #Start off assuming a swap did not occur
        swap_occurred = False
        
        #For every item in the list except the last one...
        for i in range(len(lst) - 1):

            #If the item should swap with the next item...
            if lst[i] > lst[i + 1]:

                #Then, swap them! But these lines aren't
                #quite right: fix this code!
                temp = lst[i]
                lst[i] = lst[i + 1]
                
                lst[i + 1] = temp

                #One more line is needed here; add it!
                swap_occurred = True
    return lst

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: [1, 2, 3, 4, 5]
print(sort_with_bubbles([5, 3, 1, 2, 4]))




##explanation

def sort_with_bubbles(lst):
    
    swap_occurred = True

    while swap_occurred:
        swap_occurred = False
        
        for i in range(len(lst) - 1):

            if lst[i] > lst[i + 1]:

                #First, the swap wasn't working. The goal of
                #the swap is to store a number to a temporary
                #variable so that we can change that variable
                #and preserve the value. To do that, we need
                #to copy the list item to temp first:
                temp = lst[i]
                
                #Then change that list item to the following
                #item:
                lst[i] = lst[i + 1]
                
                #And then change the following item to temp:
                lst[i + 1] = temp
                
                #So, if the items were 5 and 4, then:
                #
                # - temp becomes 5 (lst[i])
                # - lst[i] becomes 4 (lst[i + 1])
                # - lst[i + 1] becomes 5 (temp)
                #
                #Bubble sort runs as long as swaps are happening,
                #so the last thing we need to do is record that a
                #swap indeed happened:
                swap_occurred = True

    return lst


print(sort_with_bubbles([5, 3, 1, 2, 4]))
