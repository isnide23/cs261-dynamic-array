# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Ian Snyder

import numpy as np

class DynamicArray:

    def __init__(self):
        self.capacity = 10
        self.data = np.ndarray(10, 'O')
        self.next_index = 0
        

    def is_empty(self):
        if self.next_index > 0:
            return False
        elif self.next_index <= 0:
            return True

    def __len__(self):
        return self.next_index

    def __getitem__(self,index):
        return self.data[index] 

    def append(self, i):
        self.data[self.next_index] = i
        self.next_index += 1 

    
    



        

    


    