#!/usr/bin/env python3
"""

Name: TODO Add Your Name Here

Program 2: Dictionary Operations and Manipulation
This program demonstrates working with dictionaries, including creating,
accessing, modifying, and iterating through key-value pairs.
"""

def main():
    """
    Main function to demonstrate dictionary operations.
    """
    
    print("=" * 50)
    print("Program 2: Dictionary Operations")
    print("=" * 50)
    
    # STEP 1: Create a student information dictionary
    # Hint: Include keys for name, age, major, gpa
    print("\nSTEP 1: Creating a dictionary")
    student = {}  # TODO: Create a dictionary with student information
    print(f"Student information: {student}")
    
    # STEP 2: Access and print individual values
    # Hint: Use bracket notation or .get() method
    print("\nSTEP 2: Accessing dictionary values")
    # TODO: Print the student's name
    
    # TODO: Use .get() to safely access the "email" key (with a default value)
    
    
    # STEP 3: Add and update dictionary entries
    print("\nSTEP 3: Modifying the dictionary")
    # TODO: Add a new key "year" with value "Junior"
    
    # TODO: Update the age to be 1 year older
    
    # TODO: Add an "email" field with appropriate value
    
    print(f"Updated student: {student}")
    
    # STEP 4: Remove a dictionary entry
    print("\nSTEP 4: Removing entries")
    # TODO: Remove the "gpa" key using del or pop()
    
    print(f"After removal: {student}")
    
    # STEP 5: Iterate through dictionary
    print("\nSTEP 5: Iterating through dictionary")
    # Create a course grades dictionary
    grades = {"Math": 95, "English": 88, "Science": 92, "History": 85}
    
    # TODO: Print all keys
    
    
    # TODO: Print all values
    
    
    # TODO: Print all key-value pairs in a formatted way using .items()
    
    
    # STEP 6: Dictionary comprehension for grade conversion
    print("\nSTEP 6: Grade point conversion")
    # TODO: Create a new dictionary that converts percentage grades to 4.0 scale
    # Hint: Use formula: (grade / 100) * 4.0
    grade_points = {}
    print(f"Grade points: {grade_points}")
    
    # STEP 7: Check membership
    print("\nSTEP 7: Checking if keys exist")
    # TODO: Check if "Physics" is in the grades dictionary
    
    # TODO: Check if "Math" is in the grades dictionary
    
    
    print("\n" + "=" * 50)
    print("Program 2 Complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
