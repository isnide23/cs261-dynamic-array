import numpy as np

# When do I use an array?
# Here's one programming situation where your intuition should lead
# you to reach for an array. (In this situation, we'll use a Python list, which is a dynamic array.)

# fruit1 = 'Apple'
# fruit2 = 'Banana'
# fruit3 = 'Cherry'
# fruit4 = 'Donut'
# fruit5 = 'Elderberry'
# fruit6 = 'Fig'
# fruit7 = 'Grape'
# fruit8 = 'Honeydew Melon'
# fruit9 = 'Ice Cream'

# print(fruit1)
# print(fruit2)
# print(fruit3)
# print(fruit4)
# print(fruit5)
# print(fruit6)
# print(fruit7)
# print(fruit8)
# print(fruit9)

# Refactor this code using a Python list. Your program should
# exhibit the same behavior as above, but with far less code.

#fruit_basket = ['Apple', 'Banana', 'Cherry', 'Donut', 'Elderberry', 'Fig', 'Grape', 'Honeydew Melon', 'Ice Cream']

fruit_basket = np.array(['Apple', 'Banana', 'Cherry', 'Donut', 'Elderberry', 'Fig', 'Grape', 'Honeydew Melon', 'Ice Cream'])

for i in fruit_basket:
    print(i)

myList = (2, 4, 6, "yay")

print(myList)

"""
The time complexity for the for loop would be O(n) 
Since the for loop prints each item once from beginning to end, where the size
of the array is n, the time complexity should be O(n). There is a linear relationship
for time complexity as the arrays get larger.
"""









# For an extra challenge, use a numpy ndarray, which is a true
# static array.
