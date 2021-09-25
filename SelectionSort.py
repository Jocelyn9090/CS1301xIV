#We've written the function, sort_with_select, below. It takes
#in one list parameter, a_list. Our version of selection sort
#involves finding the minimum value and moving it to an
#earlier spot in the list.
#
#However, some lines of code are blank. Complete these lines
#to complete the selection_sort function. You should only need
#to modify the section marked 'Write your code here!'

def sort_with_select(a_list):
    
    #For each index in the list...
    for i in range(len(a_list)):
        
        #Assume first that current item is already correct...
        minIndex = i

        #For each index from i to the end...
        for j in range(i + 1, len(a_list)):
            
            #Complete the reasoning of this conditional to
            #complete the algorithm! Remember, the goal is
            #to find the lowest item in the list between
            #index i and the end of the list, and store its
            #index in the variable minIndex.
            #
            #Write your code here!
            if a_list[minIndex] > a_list[j]:
                minIndex = j
        #Save the current minimum value since we're about
        #to delete it
        minValue = a_list[minIndex]
        
        #Delete the minimum value from its current index
        del a_list[minIndex]
        
        #Insert the minimum value at its new index
        a_list.insert(i, minValue)
    
    #Return the resultant list
    return a_list
	

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print: [1, 2, 3, 4, 5]
print(sort_with_select([5, 3, 1, 2, 4]))



##explanation

def sort_with_select(a_list):
    
    for i in range(len(a_list)):
        
        minIndex = i

        for j in range(i + 1, len(a_list)):
            
            #The loops above already take care of the overall
            #control flow of selection sort: all we need to do
            #here is see if the current item is lower than the
            #lowest-found item on the current iteration. So,
            #we check the current item against the lowest-found
            #item so far:
            if a_list[j] < a_list[minIndex]:
                
                #And if it's lower, we note that this is the new
                #lowest-found item:
                minIndex = j

        minValue = a_list[minIndex]
        
        del a_list[minIndex]
        
        a_list.insert(i, minValue)
    
    return a_list
	


print(sort_with_select([5, 3, 1, 2, 4]))


