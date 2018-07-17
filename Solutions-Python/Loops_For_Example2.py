import random as r; # Import Library to enable random number generation 

term = r.randint(1,7);             # Choose initial Value for a Sequence term. 
Number_of_terms = r.randint(5,10); # Choose how many Sequence terms to compute. 

# Make public Initial Starting Value & Number of terms to compute. 
print "Initial Sequence Value is: " + str(term);
print "Number of terms to compute is: " + str(Number_of_terms);

for term_count in range(1,Number_of_terms + 1): # For each term: 
    if term_count % 2 == 0:           # If the term is even, 
        term = 2 * term;              # multiply by 2, 
    else:                             # otherwise, 
        term = term - 2;              # subtract 2. 

    print "Term " + str(term_count) + " is " + str(term); # Print the New Term.
 

