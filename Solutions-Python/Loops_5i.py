#!/usr/bin/python

def fib(n):

#
# A function to return the nth Fibonacci Number using recursion
# -------------------------------------------------------------
#
# PSEUDO-CODE:
# ============
#
# if n is less then 1 then return error
#
# if n is 1 or 2 then by convention, the answer is 1, so return 1
#
# otherwise return the sum of the previous 2 fibonacci numbers
#

    if n < 1:      # fib is not defined for anything less than 1,
        return -1; # so return an Error Code

    if n <= 2:
        return  1; # The first 2 Fibonacci Numbers are 1
    else:
        return fib(n-1) + fib(n-2)
                   # Otherwise Return the sum of the
                   # previous 2 Fibonacci Numbers
# TEST BED:
# =========

print fib(24);    # expect ? dunno,, too hard!!
print fib(6);     # expect 8 (1 1 2 3 5 8 ... )
print fib(10);    # expect 55 (1 1 2 3 5 8 13 21 34 55 89... )
print fib(11);    # expect 89 (1 1 2 3 5 8 13 21 34 55 89... )
print fib(1);     # expect 1
print fib(2);     # expect 1
print fib(0);     # expect -1
print fib(-5);    # expect -1


