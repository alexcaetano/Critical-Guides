############################################################
#
# Ask the Question.
# Get the answer.
# If Yes    ..... rejoice!
# If No     ..... weep!
# Otherwise ..... Error!!!!!


# Data Structures
# ===============

# Many ways to say Yes ... Maybe a tuple of all?
#                          To test response against
# Many ways to say No  ... Maybe a tuple of all?
#                          To test response against
############################################################

Yes = ('Y', 'y', 'yes', 'Yes', 'YES');
No  = ('N', 'n', 'no' , 'No' , 'NO' );

Response = raw_input("Do you understand Loops yet???");
print Response;

if   Response in Yes:
    print "Jolly Good!";
elif Response in No:
    print "Well, Try harder!";
else:
    print "Answer must be Yes or No!";


