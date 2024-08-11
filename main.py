# Sort the list 

list1 = [5,3,4,6,1]

# Method 1:
sorted(list1)
# Method 2:
list1.sort()


#create a Statement that will print out words that start with 's':

st1 = 'Print only the words that start with s in this sentence'

for word in st1.split():
    if word[0] == 's':
        print(word)


#Go through the string below and if the length of a word is even print "even!"

st2 = 'Print every word in this sentence that has an even number of letters'

for word in st2.split():
    if len(word)%2 == 0:
        print(word+" <-- has an even length!")

#checks whether a word or phrase is palindrome or not.

def palindrome(s):
    
    s = s.replace(' ','') # This replaces all spaces ' ' with no space ''. (Fixes issues with strings that have spaces)
    return s == s[::-1]   # Check through slicing