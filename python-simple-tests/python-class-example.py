import math
import numpy as np

class book_shop:

    # constructor
    def __init__(self, title):
        self.title = title

    # Sample method
    def book(self):
        print('The title of the book is', self.title)


b = book_shop('Sandman')
b.book()
# The tile of the book is Sandman


try:
    num1 = int(input('Enter Numerator: '))
    num2 = int(input('Enter Denominator: '))
    division = num1/num2
    print(f'Result is: {division}')
except:
    print('Invalid input!')
else:
    print('Division is successful.')

def str_replace(string, char):

    result = ''

    for i in string:
        if i == " ":
            i = char
            print (i)
        result = result + i
    print (result)
    
        
str1 = "l vey u"     
ch1 = "o"
str_replace(str1, ch1)


# Given a positive integer num, 
# write a function that returns True if num is a perfect square else False.

def test_num(nmr):
    result = math.sqrt(nmr) 
    print (result)
    test = int(result)
    print (test ** 2)
    if test ** 2 == nmr:
        print ("samesies")
    else:
        print ("diff")

test_num(36)
test_num(143)

# You are provided with a large string and a dictionary of the words. 
# You have to find if the input string can be segmented into words using the dictionary or not.  

string_example = 'denvernuggets'
string_example2 = 'losangeleslakers'
string_example3 = 'losangelesclippers'

my_dic = ['denver', 'nuggets', 'los', 'angeles', 'lakers']

# def my_string_segm(word):
#     sub1 = ''
#     sub2 = ''
#     for i in word:
        
#         sub1 = sub1 + i 
#         sub2 = 


########################


original_dict = {"one": 1, "two": 2, "three": 3}

reversed_dict = {}

for key, value in original_dict.items():
    reversed_dict[value] = key
print(reversed_dict)

squares = []

for i in range(5):
  squares.append(i ** 2)
print(squares)

def get_even_numbers(numbers):

    even_numbers = [x for x in numbers if x % 2 == 0]

    print(even_numbers) 

get_even_numbers ([2, 3, 4, 5, 6, 7, 8])


# Given a list of numbers, find the maximum number.

numbers = [2, 3, 4, 5, 6]

def find_max_num(numlist):
    max_val = 0
    for n in numlist:
        if max_val > n:
            continue
        else:
            max_val = n
    print (max_val)
find_max_num(numbers)

# Given a string, reverse the string.
str_example = 'Annapolis'
str_example2 = 'desserts'

def reverse_string(word):
    reversed_string = ""
    len_st = len(word) - 1
    while len_st >= 0:
        reversed_string = reversed_string + word[len_st]
        len_st = len_st - 1

    print (reversed_string)

reverse_string(str_example)
reverse_string(str_example2)

# Given a string, find the longest substring without repeating characters.

def find_long_substring (word):
    print (f"Evaluating substrings for {word}")
    long_substring = ""

    word_len = len (word)
    max_len = 0
     
    for l in word:
        if l in long_substring:
            if max_len < len(long_substring):
                max_len = len(long_substring)
                print (long_substring)

            long_substring = ""
            continue
        else:
            long_substring = long_substring + l
    print (long_substring)
    print (max_len)
    
    return max_len
find_long_substring('lollapalooza')



# Given a list of numbers, find the sum of all the numbers.
lis_num = [1, 2, 3, 34, 52, 51, 321]

def sum_nums(nos):
    sum_result = 0
    
    for n in nos:
        sum_result = sum_result + n
    print (sum_result)
    return sum_result

sum_nums(lis_num)

# Given a list of numbers, find the average of all the numbers.

def average_nums(nos):
    avg_result = 0
    
    avg_result = sum_nums(lis_num) / len(nos)
    print (avg_result)
    return avg_result

average_nums(lis_num)