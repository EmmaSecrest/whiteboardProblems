'''
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
'''
def solutions(s):
    split_string = [s[i:i+2] for i in range(0, len(s), 2)]
    for i, string in enumerate(split_string):
      if len(string) == 1:
            split_string[i] = string + '_'
            print(split_string[i])
    
    return split_string

print("abc => ", solutions('abc'))
print("abcdef => " ,solutions("abcdef"))