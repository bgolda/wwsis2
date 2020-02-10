import numpy as geek 
import random

#task1
print("@@@ TASK 1 @@@\n")
def invertList(list):
	for i in range(1, len(list)):
		list.insert(i - 1, list.pop(len(list) - 1))

list = []
list_len = int(input("Please provide length of the list: "))

for i in range(list_len):
	value = int(input("Please provide value: "))
	list.append(value)

#list = random.sample(range(1, 100), 10)
print("\nList with random values: ", list); 
invertList(list)
print ("Reverse order: ", list, "\n")

#task2
print("@@@ TASK 2 @@@\n")
sum = 0
num1 = 1
num2 = 2
num3 = 0

while num3 < 4000000:
	num3 = num1 + num2
	num1 = num2
	num2 = num3

	if num3 % 2 == 0:
		sum += num3
		print(f"Even fib num: {num3}")
print(f"Sum = {sum}\n")

#task 4
print("@@@ TASK 4 @@@\n")
def insertionSort(array): 
    for i in range(1, len(array)): 
        
        check = array[i]
        
        j = i-1
        while j >= 0 and check < array[j] : 
                array[j + 1] = array[j] 
                j -= 1
        array[j + 1] = check
  
array = random.sample(range(1, 100), 10)
print("Array with random values: ", array); 
insertionSort(array)
print ("Ascending order: ", array)
