# -----------------------------REGEX---------------------------
# What? 
# regular expression are used for searching for matching patterns within strings 
# a REGEX looks like "\w+(?<=pre)" this RegEx is used like: re.findall(regexPattern,string) 
# It is like a who new programming language that you need to learn for optimising string search

"""
How to use RegEx?  

---------RegEx characters ---------
    [] -a set of characters  
    {} -exactly the specified number of occurances of a character (e.g: "be{2}r"--matches beer NOT beeeer, ber )
    {n,} -at least the specified number of occurances of a character (e.g: "be{2,}r"--matches beer,beeeer NOT ber )
    {x,y} -specify a range of the specified charancter of occurances of a character (e.g: "be{2,3}r"--matches beer,beeer NOT beeeer,ber )
    
    \ -Signals a special sequence (can also be used to escape special characters)
    . -any character (except a new line char) (e.g. "he..o")
    ^ -string starts with... (e.g. "^Hello") (also used to exclude characters "h[^ip]o")
    $ -string ends with... (e.g. "planet$")
    * -put after a character to indicate that the character may either not match at all or can match many times (e.g. "be*r" --matches with br,ber,beer)
    ? -indicates that a character is optional (e.g. "colou?r" matches--colour,color)
    | -logical or (e.g. "hello|hallo")
    + - put after character to indicate that there is one or more occurrences (e.g. "be+r"--matches ber,beer,beeeeeeeeeer )
    () -used to capture a group
    
    e.g. search everything between and including this regex "he.*old"
 
 ----------------sequences--------------------
    [xyz] -return match if any of characters are found (represents just 1 character)
    [012] -""
    [abc][pq] -Match letter a or b or c followed by either p or q.
    [a-e] -return match within a range 
    [0-5] -""
    [a-eA-E] -return match within range lower or upper case
    
----------------Special Sequences (shortcuts)-------
    note: Capital represents an inverse of the lowercase
    \A -return a match if the specified characters are at the start of string (e.g. "\AThe")
    \Z -return match only if match is at the end of the string 
    \b -e.g. of match for '\bJessa\b' matches with 'Jessa', 'Jessa.', '(Jessa)', 'Jessa Emma Kelly' but not 'JessaKelly' or 'Jessa5'
    \B - opposite of \b
    \d -match to any digit (short for [0-9])
    \D -match to any non digit (short for [^0-9]) (e.g. '\d{4}' --will return groups of 4 digits )
    \s -match to any whitespace character (short for )
    \S -Matches any non-whitespace character. (short for [^ \t\n\x0b\r\f])
    \w -The expression \w is used to find letters, numbers and underscore characters (short for character class [a-zA-Z_0-9])
    \W -opposite of above (short for [^a-zA-Z_0-9])
    
    \1 -references:are like saying “match the same text as we did in the first group” '(a)b\1' --here \1 represents 'a'.its the same as writing 'aba'

---------Lookahead & Look behind patterns-----
    
    (?=foo) -look ahead -- 
    (?<=foo) -look behind
    (?!foo) -Negative lookahead
    (?<!foo) -Negative look behind- 
    
    e.g. 
    1) \w+(?=ssion) - This regex will match with the first part of the word in a string that ends in 'ssion' (e.g. 'EXPRE'ssion)
    2) \d{1,4} - find string-digits containing at least 1 and at most 4 numbers side by side
    3) \D[a-zA-Z]{1,4} - find non-digit text containing at least 1 and at most 4 characters side by side 
    4) \D[a-zA-Z]{1,4} - find non-digit text containing at least 1 and at most 4 characters side by side 
    5) (?:ha)-ha,(haa)-\1 -(?:)stops this group from being referenced by the \1, making the 1st reference (haa)  --matches with "ha-ha,haa-haa"
    6) (?:ha)-ha,(haa)-\1 -(?:)stops this group from being referenced by the \1, making the 1st reference (haa)  --matches with "ha-ha,haa-haa"
    7) (\*|\.) - using the escape character '\' to select special character '*' and '.'
    8) ^[0-9] -matches number only at the beginning of the string 
    9) .html$ -matches text that ends in .html
    10) .*?r -match with the first occurrence of the ending in r (lazy matching) 
"""

# REGEX in Code
from re import (
findall,
search,
split,
sub,
match,
finditer,
IGNORECASE #removes upper/lower case sensitivity
)

my_string = 'hello this is my string is '
my_long_string='re.search() function will search the regular expression pattern and return the first occurrence. Unlike Python re.match(), it will check all lines of the input string. The Python re.search() function returns a match object when the pattern is found and “null” if the pattern is not found'
num_string='12345'

# -------------------Python String Methods---------------

print(my_string.isalpha()) #are all characters in the Alphabet- spaces are included #returns FALSE due to spaces
print(num_string.isdecimal()) #is string made up of decimals between 0-9
print(my_string.isupper()) #are all char upper case 
print(my_string.islower()) #are all characters are lowercase

# find(value,start,end) method 
print(my_string.find('i'))# returns index of located string or error - remember to error handle
found= my_string.index('his')# return index of string or error 
print(found)
new_string = my_string.replace("is", 'was')

print('using the replace method...',new_string)

# --------------------REGEX Functions----------

# findall(value, SearchString)
found_all = findall('is',my_string) #return a list of found items in string or an empty list 
print('this is the findall function....',found_all)

# search(value, SearchString)
searched = search('is', my_string) #returns a match that contains a tuple variable with the start and end of match string
print('this is the search function...',searched)
print(searched.group()) #returns string
print(searched.span()) #return tuple 

# split()
list_of_string = split(',', my_string) # returns a list of strings that are split at the match
print(list_of_string)

# sub()
updated_string = sub('i', 'I', my_string,1) #returns an updated string with the replaced matches
print('sub function ....',updated_string)

# match()
matches= match('re.Match', my_long_string) #similar to search but only searches the beginning of the string and return the object or None
if matches:
    print(matches.span())#returns the tuple
else:
    print('no Matches')



# exercise
# make a function that uses REGEX to find a word at a specific occurrence in a string and replace that word with a new word.

sentence="A dogmatic dog buys dogecoin to become rich and buy hotdogs every day."

def replaceWord_func(repWord:str,newWord:str,occurrence:int,longString:str): #specifying the types of input
    allMatches = finditer(repWord,longString)#returns a callable_iterable 
    count=0
    for i in allMatches:
        count+=1
        if i.group() ==repWord and count==occurrence:
            start_Idx= i.start() #store start index 
            end_idx=i.end()#store end index
            return longString[:start_Idx] + newWord + longString[end_idx:] #reconstruct and return new string 
    
print(replaceWord_func('dog','cat',1, sentence))
