"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of numbers, like the one I used in exercise 4.0.
# 2. Process: The function adds the numbers and divides by how many there are.
# 3. Out: It returns the average, or None if the list is empty.
# 4. My function name, and why return rather than print:
#    calculate_average clearly describes what it does.
#    I use return because I can save or reuse the result in other calculations.
#    print only displays a value; it does not give the result back to the caller.


# Your code below

# My list from exercise 4.0.
list_of_numbers = [10, 9, 1, 7, 8, 6, 2, 3, 4, 5]


# This function calculates the average of a list.
def calculate_average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


# I call the same function three times with different inputs.
whole_list = calculate_average(list_of_numbers)
first_five = calculate_average(list_of_numbers[:5])
last_five = calculate_average(list_of_numbers[5:])

print("Average of all numbers:", whole_list)
print("Average of the first five:", first_five)
print("Average of the last five:", last_five)


# Check it yourself: I also test an empty list.
empty_result = calculate_average([])
print("Average of an empty list:", empty_result)

# Expected results: 5.5, 7.0, 4.0, None.
# Check result: these four values appear when the program runs.
# An empty list returns None instead of crashing (division by zero).
# I think this is acceptable because an empty list has no average.
