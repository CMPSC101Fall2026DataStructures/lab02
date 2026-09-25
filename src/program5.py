#!/usr/bin/env python3
"""

Name: TODO Add Your Name Here

Program 5: Dictionary Comprehensions
This program demonstrates dictionary comprehensions for creating and
transforming dictionaries efficiently and elegantly.
"""

def main():
    """
    Main function to demonstrate dictionary comprehensions.
    """
    
    print("=" * 50)
    print("Program 5: Dictionary Comprehensions")
    print("=" * 50)
    
    # STEP 1: Basic dictionary comprehension
    print("\nSTEP 1: Creating a number-square dictionary")
    # Traditional way
    squares_dict_traditional = {}
    for x in range(1, 6):
        squares_dict_traditional[x] = x ** 2
    print(f"Traditional way: {squares_dict_traditional}")
    
    # TODO: Create the same dictionary using dictionary comprehension
    squares_dict_comprehension = {}
    print(f"Dict comprehension: {squares_dict_comprehension}")
    
    # STEP 2: Dictionary from two lists
    print("\nSTEP 2: Creating dictionary from lists")
    names = ["Alice", "Bob", "Charlie", "David"]
    ages = [20, 22, 21, 23]
    # TODO: Create a dictionary mapping names to ages using dictionary comprehension
    # Hint: Use zip() to pair names and ages
    name_age_dict = {}
    print(f"Name-age dictionary: {name_age_dict}")
    
    # STEP 3: String lengths dictionary
    print("\nSTEP 3: Mapping words to their lengths")
    words = ["python", "programming", "data", "structures", "comprehension"]
    # TODO: Create a dictionary with words as keys and their lengths as values
    word_lengths = {}
    print(f"Word lengths: {word_lengths}")
    
    # STEP 4: Filtering dictionary with condition
    print("\nSTEP 4: Filtering with conditions")
    numbers = list(range(1, 11))
    # TODO: Create a dictionary of only even numbers and their squares
    even_squares = {}
    print(f"Even numbers and squares: {even_squares}")
    
    # STEP 5: Temperature conversion
    print("\nSTEP 5: Temperature conversion (Celsius to Fahrenheit)")
    celsius_temps = {"morning": 20, "afternoon": 25, "evening": 18, "night": 15}
    # TODO: Convert all temperatures to Fahrenheit using dictionary comprehension
    # Formula: F = C * 9/5 + 32
    fahrenheit_temps = {}
    print(f"Celsius: {celsius_temps}")
    print(f"Fahrenheit: {fahrenheit_temps}")
    
    # STEP 6: Swapping keys and values
    print("\nSTEP 6: Swapping keys and values")
    original = {"a": 1, "b": 2, "c": 3, "d": 4}
    # TODO: Create a new dictionary with keys and values swapped
    swapped = {}
    print(f"Original: {original}")
    print(f"Swapped: {swapped}")
    
    # STEP 7: Grade conversion
    print("\nSTEP 7: Converting percentage grades to letter grades")
    grade_percentages = {
        "Alice": 95,
        "Bob": 87,
        "Charlie": 76,
        "David": 92,
        "Eve": 68
    }
    
    # TODO: Create a dictionary converting percentages to letter grades
    # A: >= 90, B: >= 80, C: >= 70, D: >= 60, F: < 60
    # Hint: Use if-else expression in comprehension
    letter_grades = {}
    print(f"Percentages: {grade_percentages}")
    print(f"Letter grades: {letter_grades}")
    
    # STEP 8: Nested dictionary transformation
    print("\nSTEP 8: Product price calculation with tax")
    products = {
        "laptop": 999.99,
        "mouse": 29.99,
        "keyboard": 79.99,
        "monitor": 299.99
    }
    tax_rate = 0.08
    
    # TODO: Create a dictionary with product prices including 8% tax
    prices_with_tax = {}
    print(f"Original prices: {products}")
    print(f"Prices with tax: {prices_with_tax}")
    
    # STEP 9: Conditional dictionary building
    print("\nSTEP 9: Building dictionary with multiple conditions")
    # TODO: Create a dictionary of numbers 1-20 where:
    # - Key is the number
    # - Value is "fizzbuzz" if divisible by both 3 and 5
    # - Value is "fizz" if divisible by 3
    # - Value is "buzz" if divisible by 5
    # - Value is the number itself otherwise
    fizzbuzz_dict = {}
    print(f"FizzBuzz dictionary: {fizzbuzz_dict}")
    
    print("\n" + "=" * 50)
    print("Program 5 Complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
