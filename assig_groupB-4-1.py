numbers = [23, 89, 12, 67, 45]
numbers.sort(reverse=True)
print("Sorted numbers (largest to smallest):", numbers)

strings = ["apple", "banana", "cherry", "kiwi", "melon", "mango"]
strings.sort(reverse=True)
print("Sorted strings (reverse alphabetical order):", strings)

fruits = ["apple", "banana", "cherry", "kiwi", "melon", "mango"]

for i, fruit in enumerate(fruits):
    print(f"Position {i}: {fruit}")

fruits.insert(0, "Orange")
new_list = fruits.copy()
print("Fruits after inserting 'Orange':", fruits)
print("Copied list:", new_list)

fruits.remove("cherry")
print("Fruits after removing 'cherry':", fruits)
print("Original copied list:", new_list)

print("Third, fourth, and fifth items:", fruits[2:5])

if "apple" in fruits:
    print("Apple is present in the list.")
else:
    print("Apple is not present in the list.")

print("All items in the list:")
for fruit in fruits:
    print(fruit)

removed_item = fruits.pop(3)
print(f"Removed item at index 3: {removed_item}")
print("Final list:", fruits)