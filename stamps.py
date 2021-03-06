# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def stamps(pence):
    # Your code here
    if pence >= 5:
        if pence % 5 == 0:
            return pence / 5, 0, 0
        else:
            fives = pence / 5
            remainder = pence % 5
            if remainder % 2 == 0:
                return fives, remainder / 2, 0
            else:
                twos = remainder / 2
                return (fives, twos, remainder % 2)
    elif pence >= 2:
        if pence >= 2:
            if pence % 2 == 0:
                return 0, pence / 2, 0
            else:
                twos = pence / 2
                remainder = pence % 2
                return 0, twos, remainder
    elif pence > 0:
        return (0,0,pence)
    else:
        return (0,0,0)

print stamps(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element(p, val):
    if val not in p:
        return -1
    else:
        return p.index(val)

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1