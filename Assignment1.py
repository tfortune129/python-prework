#Question 1: Write a function to print "hello_USERNAME!" 
#USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    """Display greeting"""""
    print ("Hello_" + user_name.upper() + "!")
hello_name('honeybee222')

###########################################

#Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
"""establish range (empty)"""
oddvalues = []
def first_odds(range):
    """set parameters starting at first position of list"""
    if range[0] % 2 == 1:
        oddvalues.append(range[0])
    if len(range) > 1:
        first_odds(range[1:])
first_odds(range(1,100))
print (oddvalues)    

#--or--

def odds(value):
    return value % 2 == 1
set = [1,2,3,4,5,6,7]
result = filter(odds, set)
print (list(result))

#--or--

def oddnumbers(numbers):
    odd_num = []
    for number in numbers:
        if number % 2 == 1:
            odd_num.append(number)
    return odd_num
nums = [1,2,3,4,5,6,7,8,9,10]
print (oddnumbers(nums))

###########################################

#Question 3: Please write a Python function, max_num_in_list to return the max number of a given list. 
#The first line of the code has been defined as below.
def max_num_in_list(a_list):
    """assign first element as maxnum"""
    maxnum = a_list[0]
    for num in a_list:
        if num > maxnum:
            maxnum = num
    return maxnum

a_list = [40,4223,124,29,675,623,23,100,81]
print (max_num_in_list(a_list))
 
 #--or--

def max_num(list):
    """use built-in maxz"""
    print (max(list))
list = [40,4223,12955,29,675,623,23,100,81]
max_num(list)

###########################################

#Question 4: Write a function to return if the given year is a leap year. 
#A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
#The return should be boolean Type (true/false).

def is_leap_year(a_year):
    """set parameters for leap year"""
    if a_year % 4 == 0 and a_year % 100 != 0 or a_year % 400 == 0:
        return True  
    else: 
        return False
print (is_leap_year(2024))

###########################################

#Question 5: Write a function to check to see if all numbers in list are consecutive numbers. 
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
#The return should be boolean Type.

def is_consecutive(a_list_ofnums):
    consecutives = True
    nums = len(a_list_ofnums)
    """set exclusions:"""
    for num in range(nums - 1):
        if a_list_ofnums[num] + 1 != a_list_ofnums[num + 1]:
            consecutives = False
    return consecutives

list1 = [1,2,3,4,5]
list2 = [1,2,4,5,6]

print(is_consecutive(list1))
print(is_consecutive(list2))

