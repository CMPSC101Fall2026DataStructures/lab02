#!/usr/bin/env python3
"""

Name: TODO Add Your Name Here

Program 3: Set Operations and Manipulation
This program demonstrates working with sets, including creation,
mathematical operations, and practical applications for unique collections.
"""

def main():
    """
    Main function to demonstrate set operations.
    """
    
    print("=" * 50)
    print("Program 3: Set Operations")
    print("=" * 50)
    
    # STEP 1: Create sets and remove duplicates
    print("\nSTEP 1: Creating sets from lists")
    # Create a list with duplicate values
    numbers_with_dupes = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]
    # TODO: Convert the list to a set to remove duplicates
    unique_numbers = None
    print(f"Original list: {numbers_with_dupes}")
    print(f"Unique numbers: {unique_numbers}")
    
    # STEP 2: Add and remove elements
    print("\nSTEP 2: Adding and removing set elements")
    colors = {"red", "blue", "green"}
    # TODO: Add "yellow" to the set
    
    # TODO: Add "purple" to the set
    
    print(f"After adding: {colors}")
    
    # TODO: Remove "blue" using .remove()
    
    # TODO: Use .discard() to safely remove "orange" (won't error if not present)
    
    print(f"After removing: {colors}")
    
    # STEP 3: Set mathematical operations
    print("\nSTEP 3: Set operations - Students in classes")
    class_a = {"Alice", "Bob", "Charlie", "David", "Eve"}
    class_b = {"Charlie", "David", "Frank", "Grace", "Hannah"}
    
    print(f"Class A: {class_a}")
    print(f"Class B: {class_b}")
    
    # TODO: Find students in BOTH classes (intersection)
    both_classes = None
    print(f"\nStudents in both classes: {both_classes}")
    
    # TODO: Find students in ONLY class A (difference)
    only_a = None
    print(f"Students only in class A: {only_a}")
    
    # TODO: Find ALL unique students (union)
    all_students = None
    print(f"All students: {all_students}")
    
    # TODO: Find students in exactly ONE class (symmetric difference)
    one_class_only = None
    print(f"Students in exactly one class: {one_class_only}")
    
    # STEP 4: Set membership testing
    print("\nSTEP 4: Fast membership testing")
    # TODO: Check if "Alice" is in class_a
    
    # TODO: Check if "Frank" is in class_a
    
    
    # STEP 5: Practical application - Finding unique words
    print("\nSTEP 5: Finding unique words in text")
    text = "the quick brown fox jumps over the lazy dog the fox is quick"
    words = text.split()
    # TODO: Create a set of unique words
    unique_words = None
    print(f"Original text: {text}")
    print(f"Unique words: {unique_words}")
    print(f"Number of unique words: {len(unique_words) if unique_words else 0}")
    
    # STEP 6: Set comprehension
    print("\nSTEP 6: Set comprehension")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # TODO: Create a set of squares of even numbers using set comprehension
    even_squares = None
    print(f"Squares of even numbers: {even_squares}")
    
    print("\n" + "=" * 50)
    print("Program 3 Complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
