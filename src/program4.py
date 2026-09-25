#!/usr/bin/env python3
"""

Name: TODO Add Your Name Here

Program 4: List Comprehensions
This program demonstrates the power of list comprehensions for creating
and transforming lists in a concise, readable way.
"""

def main():
    """
    Main function to demonstrate list comprehensions.
    """
    
    print("=" * 50)
    print("Program 4: List Comprehensions")
    print("=" * 50)
    
    # STEP 1: Basic list comprehension
    print("\nSTEP 1: Creating a list of squares")
    # Traditional way
    squares_traditional = []
    for x in range(1, 11):
        squares_traditional.append(x ** 2)
    print(f"Traditional way: {squares_traditional}")
    
    # TODO: Create the same list using list comprehension
    squares_comprehension = []
    print(f"List comprehension: {squares_comprehension}")
    
    # STEP 2: List comprehension with condition
    print("\nSTEP 2: Filtering even numbers")
    numbers = list(range(1, 21))
    # TODO: Create a list of only even numbers from 1-20 using list comprehension
    evens = []
    print(f"Even numbers: {evens}")
    
    # STEP 3: String transformation
    print("\nSTEP 3: Converting strings to uppercase")
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    # TODO: Create a list of uppercase fruit names using list comprehension
    fruits_upper = []
    print(f"Original: {fruits}")
    print(f"Uppercase: {fruits_upper}")
    
    # STEP 4: Extract specific elements
    print("\nSTEP 4: Extracting first characters")
    words = ["Python", "Java", "Ruby", "JavaScript", "Go"]
    # TODO: Create a list of first letters of each word using list comprehension
    first_letters = []
    print(f"Words: {words}")
    print(f"First letters: {first_letters}")
    
    # STEP 5: Mathematical operations with conditions
    print("\nSTEP 5: Numbers divisible by 3 or 5")
    # TODO: Create a list of numbers from 1-50 that are divisible by 3 OR 5
    divisible = []
    print(f"Numbers divisible by 3 or 5: {divisible}")
    
    # STEP 6: Creating tuples with comprehension
    print("\nSTEP 6: Creating number-square pairs")
    # TODO: Create a list of tuples (number, square) for numbers 1-10
    # Example output: [(1, 1), (2, 4), (3, 9), ...]
    number_square_pairs = []
    print(f"Number-square pairs: {number_square_pairs}")
    
    # STEP 7: Nested list comprehension (Advanced)
    print("\nSTEP 7: Creating a multiplication table")
    # TODO: Create a 5x5 multiplication table using nested list comprehension
    # Hint: [[row * col for col in range(1, 6)] for row in range(1, 6)]
    mult_table = []
    print("Multiplication table:")
    for row in mult_table:
        print(row)
    
    # STEP 8: Flattening a nested list
    print("\nSTEP 8: Flattening a nested list")
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # TODO: Flatten the nested list using list comprehension
    # Hint: [item for sublist in nested_list for item in sublist]
    flattened = []
    print(f"Nested: {nested_list}")
    print(f"Flattened: {flattened}")
    
    # STEP 9: Using if-else in comprehension
    print("\nSTEP 9: Labeling numbers as even or odd")
    numbers = list(range(1, 11))
    # TODO: Create a list of "even" or "odd" labels using if-else in comprehension
    labels = []
    print(f"Numbers: {numbers}")
    print(f"Labels: {labels}")
    
    print("\n" + "=" * 50)
    print("Program 4 Complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
