# -*- coding: utf-8 -*-
"""Search Algorithms.ipynb

##Linear Search - O(n)
"""

input_list = input('Enter the numbers by spaces separated').split()
print(input_list)
search_number = int(input('Enter your number to search  '))
for i in input_list:
  if int(i) == search_number:
    print('Found')
    break
else:
  print('Not Found')

"""##Binary Search takes O(log(n)) and sorting takes O(nlogn), total = O(nlogn)"""

import random

#Generte random integer list
def generate_random_list(n):
  random_list = []
  for i in range(n):
    random_list.append(random.randint(1,10))
  return random_list

#Binary search, O(logn)
def binary_search(input_list, search_number):
  low = 0
  high = len(input_list) - 1
  while low <= high:
    mid = (low + high) // 2
    if input_list[mid] == search_number:
      print('Element Found')
      return
    elif search_number > input_list[mid]:
      low = mid + 1
    else:
      high = mid - 1
  return -1

search_list = generate_random_list(5)
print(search_list)

#Binary search needs list to be sorted, O(nlogn)
search_list.sort()

print(search_list)
search_num = int(input('Enter your number to search  '))
binary_search(search_list, search_num)
