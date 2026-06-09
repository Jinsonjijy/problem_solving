"""

append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

"""
arr=["toyo","che","mak"]
arr[0]="suk"# array can be manipulated using the index
print(arr)
arr.append("sukar")
n=len(arr)
arr.pop(0)
arr.remove("che")
print(arr)
# arr.clear()
# print(arr)
arr1=arr.copy()# in the case of copy it only return a copy not the entire refernce or instance
arr1.pop(0)
print(arr,arr1)
print(arr.count("mak"))
arr.extend(arr1)
print(arr)
print(arr.index("sukar"))
arr.insert(1,"makar")
print(arr)
arr.remove("makar")
print(arr)
arr.reverse()
print(arr)
print(sorted(arr))
