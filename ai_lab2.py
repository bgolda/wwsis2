import numpy as geek 
import random

def insertionSort(array): 
    for i in range(1, len(array)): 
        
        check = array[i]
        
        j = i-1
        while j >= 0 and check < array[j] : 
                array[j + 1] = array[j] 
                j -= 1
        array[j + 1] = check 
  
array = random.sample(range(1, 100), 10)
print("Array with random values:\n", array); 
insertionSort(array)
print ("Ascending order:")
for i in range(len(array)):
    print (array[i], end=', ', flush=True)