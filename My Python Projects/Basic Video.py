import random
import sys
import os

grocery_list = ['Juice', 'Carrot', 'Potatoes']
other_events = ['Wash Car', 'Cash Check', 'Feed dog']
grocery_list[0] = 'Green Juice'
grocery_list.append('Onions')
grocery_list.insert(1, 'Cat Food')
grocery_list.sort()
print('First grocery item is ' + grocery_list[0] + '.')

print(grocery_list[1:3])

to_do_list = [other_events, grocery_list]
print(to_do_list)

print('\n' *2 + (to_do_list[1][0]))


