"""
<QUESTION 1>

    Define a function that can accept two strings as input and returns the string with maximum length to the console.

    If two strings have the same length, then the function should return both strings separated by a " ".

    In this case, the strings should be returned in the same order in which they were given.

<EXAMPLES>

    one("hi","hello") → "hello"
    one("three", "two") → "three"
    one("three", "hello") → "three hello"

<HINT>

    What was the name of the function we have seen to check the length of a container?
    Use your CLI to access the Python documentation and get help(len).
"""


def one(input1, input2):
    input1_len = len(str(input1))
    input2_len = len(str(input2))

    if input1_len == input2_len:
        output = str(f"{input1} {input2}")

    elif input1_len > input2_len:
        output = input1

    elif input1_len < input2_len:
        output = input2

    return output


"""
<QUESTION 2>
    Return the string that is between the first and last appearance of "bert" in the given string.
    Return the empty string "" if there is not 2 occurances of "bert".
    IGNORE CASE.

<EXAMPLES>

    two("bertclivebert") → "clive"
    two("xxbertfridgebertyy") → "fridge"
    two("xxBertfridgebERtyy") → "fridge"
    two("xxbertyy") → ""
    two("xxbeRTyy") → ""

<HINT>

What was the name of the function we have seen to seperate a String? How can we make a string all upper or lower case?

string.split("bert")
find index first instance of bert in list. The word we want to return is index+1.
if we have two instances of bert, there will always be an index of 2, and the word in between will always be index 1.


"""


def two(input):
    bert_input = input.lower()
    input_list = bert_input.split("bert")
    bert_count = bert_input.count("bert")

    if bert_count != 2:
        output = ""

    else:
        output = input_list[1]

    return output


"""
    <QUESTION 3>

given a number:
if this number is divisible by 3 return "fizz"
if this number is divisible by 5 return "buzz"
if this number is divisible by both 3 and 5 return "fizzbuzz"
if this number is not divisible by 3 or 5 return "null"

    <EXAMPLES>

three(3) → "fizz"
three(10) → "buzz"
three(15) → "fizzbuzz"
three(8) → "null"
"""


def three(arg1):
    fizz = 3
    buzz = 5
    output = "null"

    if arg1 % fizz == 0 and arg1 % buzz == 0:
        output = "fizzbuzz"

    elif arg1 % fizz == 0:
        output = "fizz"

    elif arg1 % buzz == 0:
        output = "buzz"

    return output


"""
<QUESTION 4>

    Given a string, seperate the string into the individual numbers present,
    then add each digit of each number to get a final value for each number
    
    String example = "55 72 86"
    
    "55" will = the integer 10
    "72" will = the integer 9
    "86" will = the integer 14
    
    You then need to return the highest value, in the example above this would be 14.

<EXAMPLES>

    four("55 72 86") → 14
    four("15 72 80 164") → 11
    four("555 72 86 45 10") → 15
    
    double for loop.
    
    for each full_number in split_list:
        for each digit in full_number: 
                                    # convert character to an integer.
                                    # add to temp_count_list, which is inside of for loop.
                                    # sum of temp_count_list, to every_counted_full_number, which is outside of loop.
"""


def four(arg1):
    input_list = str(arg1)
    split_list = input_list.split(" ")
    every_counted_full_number = []

    for full_number in split_list:
        temp_count_list = []
        for digit in full_number:
            temp_count_list.append(int(digit))  # create temp empty list

        full_number_sum = sum(temp_count_list)
        every_counted_full_number.append(full_number_sum)

    return max(every_counted_full_number)


"""
<QUESTION 5>

    Given a large string that represents a csv, the structure of each record will be as follows:
    
    owner,nameOfFile,encrypted?,fileSize
    
    "Bert,helloWorld.py,True,1447,Bert,strings.py,False,1318,Jeff,dice.py,False,1445"
    
    For each record, if it is not encrypted, return the names of the owners of the files in a String Array.
    Do not include duplicate names.
    If all records are encrypted, return an empty Array.

<EXAMPLES>

five("Jeff,random.py,False,1445") → ["Jeff"]
five("Bert,numberGen.py,True,1447,Bert,integers.py,True,1318,Jeff,floats.py,False,1445") → ["Jeff"]
five("Bert,boolean.py,False,1447,Bert,conditions.py,False,1318,Jeff,loops.py,False,1445") → ["Bert","Jeff"]
five("Bert,prime.py,True,1447,Bert,ISBN.py,False,1318,Jeff,OOP.py,False,1445") → ["Bert","Jeff"]

Dont forget, False is a String, not a Boolean value in the Tests above.


Dev Notes:

split by ,


"""


def five(input):
    return []


"""

<QUESTION 6>

There is a well known mnemonic which goes "I before E, except after C",
which is used to determine which order "ei" or "ie" should be in a word.

Write a function which returns the boolean True if a string follows the mnemonic, and returns the boolean False if not.

<EXAMPLES>

six("ceiling") → True
six("believe") → True
six("glacier") → False
six("height") → False
"""


def six(input):
    if 'ie' in input:

        if 'cie' in input:
            output = False

        else:
            output = True

    elif 'ei' in input:

        if 'cei':
            output = True

        else:
            output = False

    return output


# <QUESTION 7>

# Write a function which returns the integer number of vowels in a given string.
# You should ignore case.

# <EXAMPLES>

# seven("Hello") → 2
# seven("hEelLoooO") → 6

# <HINTS>

# How do we ignore case in a String? help(str) may offer some insight.

def seven(input):
    return 0


# <QUESTION 8>

# Write a function which takes an input (between 1 and 10 inclusive) and multiplies it by all the numbers before it.
# eg If the input is 4, the function calculates 4x3x2x1 = 24

# <EXAMPLES>

# eight(1) → 1
# eight(4) → 24
# eight(8) → 40320

# <HINT>

# You may need to create a list of numbers from 0 to i, take a look at help(range).

def eight(input):
    return 1


# <QUESTION 9>

# Given a string and a char, returns the position in the String where the char first appears.
# Ensure the positions are numbered correctly, please refer to the examples for guidance.
# DO NOT ignore case
# IGNORE whitespace
# If the char does not occur, return the number -1.

# <EXAMPLES>

# nine("This is a Sentence","s") → 4
# nine("This is a Sentence","S") → 8
# nine("Fridge for sale","z") → -1

# <HINT>

# Take a look at the documentation for Strings, List and range.

def nine(inputString, char):
    return -1


# <QUESTION 10>

# Given a string, int and a char, return a boolean value if the 'nth'
# (represented by the int provided) char of the String supplied is the same as the char supplied.
# The int provided will NOT always be less than than the length of the String.
# IGNORE case and Whitespace.

# <EXAMPLES>

# ten("The",2,'h') → True
# ten("AAbb",1,'b') → False
# ten("Hi-There",10,'e') → False

# <HINT>

# How do we find the length of a container, take a look at help(len), you will also need to look at help(str) for String manipulation.

def ten(string, int, char):
    return False
