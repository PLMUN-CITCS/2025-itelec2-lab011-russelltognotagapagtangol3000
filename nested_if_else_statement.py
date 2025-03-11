try:
    # Get user input
    age_str = input("Enter your age: ")
    membership_str = input("Are you a member? (Yes/No): ")
    
    # Convert input
    age = int(age_str)
    membership = membership_str.strip().lower()
    
    # Nested if-else statements
    if age >= 18:
        if membership == "yes":
            print("Access granted.")
        else:
            print("Membership required for access.")
    else:
        print("Access denied. Must be at least 18 years old.")

except ValueError:
    print("Invalid age input. Please enter an integer.")
