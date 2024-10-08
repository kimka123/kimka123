#!/usr/bin/env python
# coding: utf-8

# In[1]:


##lAB ASSIGNMENT 4 AND 5
# AUTHOR: Beren Vapur
# DATE: 10/06/2024

#instructions:
# rename this file LabAssignmentFour+your lastname for eg. LabAssignmentFourDebrah

#submission:
# 1. Submit to brightspace
# 2. upload to your git account. 


# In[2]:


##Assignment Four (4) Functions

#Question One

# Write a function add_numbers(a,b) which takes two parameters adds them and returns the result.
# Don't forget to test your function

def add_numbers(a, b):
    return a + b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = add_numbers(num1, num2)

print("Sum of the numbers:", result)


# In[16]:


#Question two

# Write a function get_min_max(list_numbers) which returns the mininum and maximum of values from the list
# Don't forget to test your function


my_list = [3, 8, 4, 1, 5, 9, 2]

minimum_number = min (my_list)
maximum_number = max (my_list)

print('the minimum number is: ',minimum_number)
print('the maximum number is:' ,maximum_number)


# In[15]:


#Question three

# Given two integers, return 'The sum of the integers equals 40' if the sum is equal to 40. If not return 'The sum is not equal to 40'
# Don't forget to test your function

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if a + b == 40:
        print ('The sum of the integers equals 40')
else:
        print ('The sum is not equal to 40')


        
        


# In[12]:


#Question four

# Write a function the prints the even numbers from a given list. 
# Don't forget to test your function.

list = [10, 21, 4, 45, 66, 93]


for num in list:

    
    if num % 2 == 0:
        print(num, end=" ")


# In[5]:


#Question five

# Write a function such that when there are two numbers passed to it only the product is return if the product 
# is equal to or lower than 500, else return their sum.
#Don't forget to test your function. 

num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))

def product_numbers(num1, num2):
    product = num1 * num2
    if product <= 500:
        return product
    else:
        return num1 + num2

result = product_numbers(num1, + num2)
print(f"The result is = ", result)



# In[4]:


#Question six

# Write a function to check if the first and the last number of a given list is the same. 
# If they are the same then return true else return false. 
nums = [5, 20, 30, 40, 10]
if nums[0] == nums[-1]:
    print('First and last numbers are the same')
else:
    print('First and last numbers are not the same')


# In[14]:


#Question seven

# Write a function which calculates the income tax when a given income take is supplied as an argument. 
# use the information below to calculate the tax required. 
# Taxable Income                     Rate(in %)
#  First $5000                        0
#  Next  $5000                        15
#  Remaining                          25

# Kindly read on how income tax is calculated. 
# Don't forget to test your function. 

def income_tax(salary):
    if salary <= 5000:
        income = 0
    
    elif salary <= 10000:
        
        income = (salary-5000) * 0.15

    else:
        income = (5000* 0.15) + ((salary-1000) * 0.25)
    return income

salary = int(input('Enter your salary:'))
income = income_tax(salary)
print(f'the income tax is {income} ')



# In[49]:


##Assignment Four (5) Data structures

#Question eight

# A. Create a dictionary called fruit_store it should be empty. 
# B. Add the following fruit-unit_price pair to the dictionary you created. 
#  "Banana":4
#  "Pear": 2
#  "Apple":3
# C. Add a new fruit-unit_price to the dictionary above 
#    "Watermelon": 6
# D. Assuming the quantity of Banana is 30, Pear is 40, Apple is 70 and finally watermelon is 60
#  i. How much is the total value of our inventory. 
# E. Print out the list of fruits and their unit_price in our store. 

fruit_store = {}


fruit_store["Banana"] = 4
fruit_store["Pear"] = 2
fruit_store["Apple"] = 3


fruit_store["Watermelon"] = 6



quantities = {
    "Banana": 30,
    "Pear": 40,
    "Apple": 70,
    "Watermelon": 60
}

total_value = sum(fruit_store[fruit] * quantities[fruit] for fruit in fruit_store)

print(f"Total value of inventory: ${total_value}")

print("\nFruit Store Inventory:")
for fruit, price in fruit_store.items():
    print(f"{fruit}: ${price} per unit")


# In[35]:


#Question nine

# Given a list numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] extract sublist [2, 3, 4] using slicing

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sublist = numbers[2:5]
print(sublist)


# In[36]:


#Question ten

# Given a list animals = ['cat', 'dog', 'rabbit', 'mouse', 'elephant', 'tiger'] replace the middle two elements with
# ['lion','skunk'] using slicing and replacing.

animals = ['cat', 'dog', 'rabbit', 'mouse', 'elephant', 'tiger']
animals[2:4] = ['lion', 'skunk']
print(animals)


# In[ ]:




