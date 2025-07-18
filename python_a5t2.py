# Task 2 : Demonstrate List Slicing

# Step 1: Create a list of numbers from 1 to 10
myList = list(range(1, 11))
print("Complete List :", myList)

# Step 2: Extract the first five elements from the list
extract_five = myList[:5]
print("Extracted first five elements:", extract_five)

# Step 3: Reverse the extracted elements

# Method 1 - Using reverse()
extract_five.reverse()
print("Method 1 (Using reverse()): Reversed extracted elements:", extract_five)

# Method 2 - Using slicing technique
extract_five.reverse() # Since, method 1 has already reversed the elements, resetting back to original elements.
reverse_five_m1 = extract_five[::-1]
print("Method 2 (Using slicing technique): Reversed extracted elements:", reverse_five_m1)

# Method 3 - Using reversed()
reverse_five_m2 = reversed(extract_five) # reverse_five_m2 will not be available as a list
reverse_five_m2 = list(reverse_five_m2) # reverse_five_m2 is now a list
print("Method 3 (Using reversed()): Reversed extracted elements:", reverse_five_m2)