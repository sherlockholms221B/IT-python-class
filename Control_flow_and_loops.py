'''
In this code, we cover the following concepts:

if-else statement: It allows the program to make decisions based on a condition.
if-elif-else statement: It provides multiple condition checks and corresponding actions.
while loop: It repeatedly executes a block of code as long as the condition is true.
for loop: It iterates over a sequence of elements (e.g., list, string, range) or an iterator.
range() function: It generates a sequence of numbers within a specified range.
break statement: It terminates the loop prematurely.
continue statement: It skips the remaining code within a loop iteration and moves to the next iteration.
Nested loops: It demonstrates the concept of having loops within loops.
else statement in loops: It executes a block of code when the loop has completed successfully without any break statements.
These examples should give you a good understanding of control flow and loops in Python. Feel free to experiment and modify the code to explore further!

If you have any more questions, feel free to ask.

'''

# Control Flow and Loops Example

# if-else statement
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

# if-elif-else statement
grade = 85
if grade >= 90:
    print("A grade")
elif grade >= 80:
    print("B grade")
elif grade >= 70:
    print("C grade")
else:
    print("Fail")

# while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# range function in loops
for num in range(1, 6):
    print(num)

# break statement
for num in range(1, 10):
    if num == 5:
        break
    print(num)

# continue statement
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# else statement in loops
for num in range(1, 6):
    print(num)
else:
    print("Loop completed successfully")