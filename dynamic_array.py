# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Ian Snyder

import numpy as np

class DynamicArray:

    def __init__(self):
        self.capacity = 10
        self.data = np.ndarray(10, 'O')
        self.next_index = 0
        self.full = False
        

    def is_empty(self):
        if self.next_index > 0:
            return False
        elif self.next_index == 0:
            return True
        # elif self.next_index < 0:
        #     print("Negative index.")
        #     pass

    def __len__(self):
        return self.next_index

    def __getitem__(self,index):
        if index >= 0 and index < self.next_index:
            return self.data[index] 
        elif index < 0 or index >= self.next_index:
            raise IndexError



    def append(self, i):
        self.data[self.next_index] = i
        self.next_index += 1 

    def clear(self):
        self.data = np.ndarray(10, 'O')
        self.next_index = 0

    def pop(self):
        if self.next_index <= 0:
            raise IndexError
        else:
            self.next_index -= 1
            return self.data[self.next_index]

    def delete(self, numX):
        if self.next_index <= 0:
            raise IndexError
        elif numX >= self.next_index or numX < 0:
            raise IndexError
        else:
            for i in range(numX, self.next_index):
                self.data[i] = self.data[i +1]
            self.next_index -= 1
            self.data[self.next_index] = None
                
    def insert(self, pos, dataX):
        if pos < 0 or pos >= self.next_index + 1:
            raise IndexError
        else:
            for i in reversed(range(pos, self.next_index + 1)):
                self.data[i + 1] = self.data[i]
            self.data[pos] = dataX          
            self.next_index += 1

    def is_full(self):
        if self.next_index < 10:
            return self.full
        elif self.next_index == 10:
            self.full = True
            return self.full
        

                

    


    
    

    
    



        

    


    