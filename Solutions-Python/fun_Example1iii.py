###########################################################################################
### A tricky one to finish!
### Change all the "["s to "("s and all the "]"s to ")"s and all the lists become tuples.
###
### AverageN does not seem to caare that it is processing tuples instead of lists!
###
### Oh, I change the Variable names also ... just to be consistent.
###
### NOT QUITE ALL!!! Note the strange "," added to the last tuple in the tuple of tuples!
### Were you to remove this comma, you would get an error message?
###
### Can you think why thhis comma should be so vital?
###
###########################################################################################

def AverageN (Numbers): # Using a Variable number of Parameters

    Total = 0.0; # Initialise Variable to store the Sum of all Arguments.

    for Number in Numbers: # For each Argument,
        Total += float(Number);   # increment the Total.

    return (Total / len(Numbers)); # Return the Average.

#TEST BED 
#======== 

Tuple_of_Tuples = ((1 , 2, 4), (0.1 , 2.95, 7), (1 , 2.6), (1 , 13.2, 9.2, 4, 6, 10), (2.9999,));

for Tuple in Tuple_of_Tuples:
    print AverageN(Tuple);
# In turn: 3 Integers, 3 Mix float/Integer, 2 Numbers, 6 Numbers, 1 Number 

