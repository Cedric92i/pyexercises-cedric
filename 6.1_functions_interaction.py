"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: My list of numbers from exercise 4.0.
# 2. Process, function by function:
#    calculate_average finds the average of the list.
#    count_above_threshold counts the numbers above that average.
#    calculate_percentage converts that count into a percentage.
#    percentage_above_average uses these three functions in that order.
# 3. Out: The percentage of numbers that are higher than the average.
# 4. The question my fourth function answers:
#    "What percentage of my numbers are above the average?"
#    Three small functions are easier to test because each has one job.


# Your code below

# I reuse the same list from exercise 4.0.
list_of_numbers = [10, 9, 1, 7, 8, 6, 2, 3, 4, 5]


# Function 1: find the average of a list.
def calculate_average(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


# Function 2: count values above a given number.
def count_above_threshold(numbers, threshold):
    count = 0
    for number in numbers:
        if number > threshold:
            count += 1
    return count


# Function 3: convert a part of a total into a percentage.
def calculate_percentage(part, total):
    if total == 0:
        return 0.0
    return (part / total) * 100


# Function 4: use all three functions to answer my question.
def percentage_above_average(numbers):
    average = calculate_average(numbers)
    if average is None:
        return 0.0
    count = count_above_threshold(numbers, average)
    return calculate_percentage(count, len(numbers))


# Check it yourself: I test each small function separately.
# Test 1: calculate_average([2, 4, 6]) should return 4.0.
print("Test 1 - average:", calculate_average([2, 4, 6]))

# Test 2: count_above_threshold([2, 4, 6], 4) should return 1.
print("Test 2 - count:", count_above_threshold([2, 4, 6], 4))

# Test 3: calculate_percentage(2, 5) should return 40.0.
print("Test 3 - percentage:", calculate_percentage(2, 5))


# Finally, I call the fourth function with my original list.
answer = percentage_above_average(list_of_numbers)
print("Percentage above the average:", answer, "%")

# Expected result: 50.0%, because 5 of my 10 numbers are above 5.5.
# Check result: the three tests give 4.0, 1, 40.0 and the final result is 50.0%.
# If the list is empty, the fourth function returns 0.0 to avoid an error.
