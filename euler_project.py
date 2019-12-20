file = open("array_lab2.txt", "r")

for line in file:
	fields = line.split(",")

fields = [f.replace('"', '') for f in fields]
#print(fields)
fields_inverted = []

for i in range(len(fields), 0, -1):
	fields_inverted.append(fields[i-1])
	fields.pop(-1)
#print(fields_inverted)

#excercise_1
#creating new empty list
new_arr = []
#number of elements declared by user
n = int(input("Enter the length of the array: "))

for i in range(0, n):
	#print(f"Please enter {arr_len} - {arr_len-1} element of the array: ")
	ele = int(input())
	new_arr.append(ele) #appending the element at the end of the list

print(new_arr)