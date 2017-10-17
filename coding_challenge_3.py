'''
Galvanize programming challenge #3  (take-home-style)

The challenge below will test your algorithm skills, your Python skills,
and your teaching skills. Please spent 1-2 hours on this challenge (we'll
go on the honor system here). We suggest you spend about 30-45 minutes
"solving" the challenge and testing your solution, then spend the remainder
of the time documenting / explaining your solution. Pretend it will be given
to students as an example of a high-quality solution which they should learn
from. When you submit your solution, let us know exactly how long you spent
preparing your solution.

All the best! Let us know if you have questions about this process.

______________________________________________________________________________

From: https://www.codewars.com/kata/sum-of-pairs

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * entire pair is earlier, and therefore is the correct answer
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]
'''

import itertools #use this to compare two items in a list

def sum_pairs(value_list, target_value):
#Initialize all variables
    a = [] #list variable to manipultate
    flag = 0 #flag to declare if the list is full or not

#Step 1: Get the variables into the temporary list
    for i,j in itertools.combinations(enumerate(value_list),2): #compare each combination  
#Step 2: If the combination is equal to the value you need, place it into the list
        value = i[1]+j[1] #check the sum of the values
#Step 3: Find out where the pair is in the sequence relative to possible other pairs                 
        if value == target_value: #if two elements will add up to the system
            if a != []: #if the list is not empty compare the elements 
            #take the variables and compare their indices
                t = a[0] # put  the list into a temporary variable
                #Take the two values that are in the list
                t1 = t[0]
                t2 = t[1] 
                #Take the indices of the two values
                x = t1[0]
                y = t2[0]                                     
                
                if x <i[0]: #if first index is lower than that of the second you must compre the second index 
                    if y >j[0]: # if the second variable index is before the second one, then that pair comes before the second
                        a.pop()#get rid of the combination that is there because an earlies combination has been found
                        a.append([i,j]) #add the combination that works to the list to be printed later
                        flag = 1  #change the flag because a solution has been found
                #if the second variable index is larger than the first varaible index, then that pair does not come earlier
                else: #this is the other case left                   
                    if y < j[0]:
                        a.pop() #get rid of the combination that is there because an earlies combination has been found
                        a.append([i,j])#add the combination that works to the list to be printed later
                        flag = 1 #change the flag because a solution has been found
            else:
                #if the list is empty, there is no combination found yet that equals the pair
                a.append([i,j]) #Add the elements to the list if it's empty
                flag = 1#change the flag because a solution has been found
#Step 4: Print out the pair and it's index based on your resoluts
    if flag == 1: #this is the flag to say that a combination was found
        print("The first pair values of "+str(a)+ " combine to make " + str(target_value) +".")
    else: #this is the 0 flag to say that no combination was found
        print("There are no pairs of values that can be added to produce "+ str(target_value)+".")    
    pass

#Step 5: Test the code
print(sum_pairs([11, 3, 7, 5],        10))
print(sum_pairs([4, 3, 2, 3, 4],       6))
print(sum_pairs([0, 0, -2, 3],         2))
print(sum_pairs([10, 5, 2, 3, 7, 5],  10))
