#!/usr/bin/env python3
"""

Name: TODO Add Your Name Here

Program 1: List Operations and Manipulation
This program demonstrates fundamental list operations including creation,
modification, and common methods for working with lists.
"""

def main():
    """
    Main function to demonstrate list operations.
    """
    
    print("=" * 50)
    print("Program 1: List Operations and Manipulation")
    print("=" * 50)
    
    # STEP 1: Create and populate a list
    # Hint: Create a list of fruits with at least 5 items
    print("\nSTEP 1: Creating a list")
    fruits = []  # TODO: Add at least 5 fruits to this list
    print(f"Original list: {fruits}")
    
    # STEP 2: Add new items to the list
    # Hint: Use append() to add "mango" and insert() to add "grape" at index 2
    print("\nSTEP 2: Adding items")
    # TODO: Add "mango" to the end of the list
    
    # TODO: Insert "grape" at index 2
    
    print(f"After adding items: {fruits}")
    
    # STEP 3: Remove items from the list
    # Hint: Use remove() to remove "banana" (if it exists) and pop() to remove the last item
    print("\nSTEP 3: Removing items")
    # TODO: Remove "banana" from the list (check if it exists first)
    
    
    # TODO: Remove and save the last item using pop()
    last_item = None
    print(f"Removed last item: {last_item}")
    print(f"After removing items: {fruits}")
    
    # STEP 4: List information and operations
    # Hint: Use len(), sum() (for numeric lists), max(), min()
    print("\nSTEP 4: List analysis")
    numbers = [15, 42, 8, 23, 67, 34, 19]
    # TODO: Print the length of the numbers list
    
    # TODO: Print the sum of all numbers
    
    # TODO: Print the maximum and minimum values
    
    
    # STEP 5: Sorting and reversing
    print("\nSTEP 5: Sorting and reversing")
    # TODO: Sort the numbers list in ascending order (use .sort())
    
    print(f"Sorted numbers: {numbers}")
    
    # TODO: Reverse the numbers list (use .reverse())
    
    print(f"Reversed numbers: {numbers}")
    
    # STEP 6: List slicing
    print("\nSTEP 6: List slicing")
    # TODO: Print the first 3 elements of the numbers list
    
    # TODO: Print the last 3 elements of the numbers list
    
    # TODO: Print every other element from the numbers list
    
    
    print("\n" + "=" * 50)
    print("Program 1 Complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
