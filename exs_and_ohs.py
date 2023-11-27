'''
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
'''

def xo(s):
    s = s.lower()
    print("is everthing lower case: ", s )
    
    number_x = s.count('x')
    print("number of x: " ,number_x)
    number_o = s.count('o')
    print("number of o: " ,number_o)

    if number_x == number_o:
        return True
    else:
        return False


#print("Result for 'ooxx': ", xo("ooxx"))
#print("Result for 'xooxx': ", xo("xooxx"))
print("Result for ooxXm: " ,xo("ooxXm"))

