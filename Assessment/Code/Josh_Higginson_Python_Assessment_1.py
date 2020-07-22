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


def two(input):
    bert_input = input.lower()
    input_list = bert_input.split("bert")
    bert_count = bert_input.count("bert")

    if bert_count != 2:
        output = ""

    else:
        output = input_list[1]

    return output


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


def six(input):
    output = None

    if 'ie' in input:
        if 'cie' in input:
            output = False

        else:
            output = True

    elif 'ei' in input:
        if 'cei' in input:
            output = True

        else:
            output = False

    return output


def seven(input):
    lower_input = input.lower()
    list_of_vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0

    for vowel in list_of_vowels:
        vowel_count += lower_input.count(vowel)

    return vowel_count


def eight(input):

    factorial = input
    factorial_list = []
    output = 1

    if input == 1:
        output = 1

    else:
        while factorial > 0:
            factorial_list.append(factorial)
            factorial = factorial - 1

        for number in factorial_list:
            output *= number

    return output

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


def ten(string, int, char):
    string = string.lower()
    char = char.lower()

    if len(string) <= int:
        output = False

    else:
        if string[int - 1] == char:
            output = True
        else:
            output = False

    return output
