# 2025-ITELEC2-LAB011
Week 04 - Conditional Statements

Laboratory # 11 - Guided Coding Exercise: Nested if...else Statements in Python

## **Instructions**

### **Step 1.1: Accept the Assignment**

   1. Click on the assignment link provided by your instructor.
   2. GitHub Classroom will create a **private repository** under your GitHub account.
   3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 1.2: Setup your Git Environment**
Only perform this if this is the first time you will setup your Git Environment

   1. Create a GitHub Account:
   ```bash
   https://github.com/signup?source=login
   ```
      
   2. Download and Install Git on your Laptop/Desktop:
   ```bash
   https://git-scm.com/downloads
   ```
   
   3. Create a Folder in your Laptop/Desktop
   4. Right-click anywhere in the created folder and select "Open Git Bash Here".
   5. In the Git Bash Terminal, set your git name, perform command:
   ```bash
   git config --global user.name "Your Name"
   ```
   
   6. In the Git Bash Terminal, set your git email, perform command:
   ```bash
   git config --global user.email "your.email@example.com"
   ```
   
   7. Create your SSH Key, just follow the instructions, no need to provide filename and passphrase. In the Git Bash Terminal, perform command:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   
   8. Copy your SSH Keys into clipboard. In the Git Bash Terminal, perform command:
   ```bash
   clip < ~/.ssh/id_rsa.pub
   ```
   
   9. Log in to your GitHub account.
   10. In the upper-right corner of GitHub, click your profile picture and select Settings.
   11. In the left sidebar, click on SSH and GPG keys.
   12. Click the New SSH key button.
   13. In the Title field, give the key a recognizable name (e.g., "My Windows Laptop").
   14. In the Key field, CTRL + V or paste the keys copied into your clipboard. Save the key.
   15. Go Back to terminal, use command:
   ```bash
   ssh -T git@github.com
   ```

### **Step 2: Clone the Repository to Your Local Machine**

   1. On your repository page, click the green **"Code"** button.
   2. Copy the repository URL (choose HTTPS for simplicity).
   3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:
   
   ```bash
   git clone <git_repo_url>
   ```
   
   4. Navigate into the cloned folder:
   
   ```bash
   cd <git_cloned_folder>
   ```

### **Step 3: Complete the Assignment**

**Laboratory # 11 - Guided Coding Exercise: Nested if...else Statements in Python**

   **Objective:**
   - Learn how to nest if...else statements to create more complex decision-making structures.
   - Understand how inner if statements depend on outer conditions.
   - Practice handling string input and performing case-insensitive comparisons.

   **Desired Output (Example 1):**
   ```bash
   Enter your age: 25
   Are you a member? (Yes/No): yes
   Access granted.
   ```
   **Desired Output (Example 2):**
   ```bash
   Enter your age: 16
   Are you a member? (Yes/No): no
   Access denied. Must be at least 18 years old.
   ```
   **Desired Output (Example 3):**
   ```bash
   Enter your age: 20
   Are you a member? (Yes/No): No
   Membership required for access.
   ```
   
   **Notable Observations (to be discussed after completing the exercise):**
   - Nested if statements allow you to check conditions within other conditions. The inner if statement's execution depends on the outer if statement's result.
   - Indentation is extremely important for nested if statements. It determines which code block belongs to which condition.
   - String comparisons in Python are case-sensitive by default. It's often good practice to convert strings to lowercase (or uppercase) before comparing them to avoid issues with different capitalization.
   - The .strip() method is useful for removing leading/trailing whitespace from user input, which can prevent unexpected behavior.

   **Python Best Practices**
   - Clear and Consistent Indentation: Correct indentation is essential for nested if statements to work correctly. Use 4 spaces for each level of indentation.
   - Input Validation and Normalization:
      - Validate numerical input (e.g., using try-except to ensure the age is a valid integer).
      - Normalize string input (e.g., convert to lowercase using .lower() and remove leading/trailing whitespace using .strip()) to handle variations in user input (e.g., "yes", "Yes", " YES ", "no", "No").
   - Descriptive Variable Names: Use clear variable names (e.g., age, is_member).
   - Comments: Add comments to explain complex logic, especially when nesting multiple levels of if statements.
   - Test Thoroughly: Test your code with various inputs to ensure it handles all possible scenarios correctly (different ages, membership status - yes/no variations).

   **Step-by-Step Instructions:**

   1. Setting up: Open your preferred Python environment or Text Editor, and create a Python Script.
      - Required Filename: `nested_if_else_statement.py`
      
   2.  Get user input:
      - Use the input() function to prompt the user for their age. Store the returned string.
      - Use the input() function to prompt the user for their membership status (Yes/No). Store the returned string.      
```python
age_str = input("Enter your age: ")
membership_str = input("Are you a member? (Yes/No): ")
```
      
   3.  Convert input:
      - Convert the age input string to an integer using int(). Store the result in the age variable.
      - Convert the membership input to lowercase and remove leading/trailing spaces using .strip().lower(). Store the result in the membership variable.
```python
age = int(age_str)
membership = membership_str.strip().lower()
```

   4. Use nested if statements:
      - Write an outer if statement to check if the age is greater than or equal to 18.
      - Inside the outer if block, write another if statement to check if the membership status is "yes".
      - Inside the inner if block, print "Access granted.".
      - Inside the outer if block, but after the inner if statement, add an else block (this else is associated with the inner if). Inside this else block, print "Membership required for access.".
      - After the outer if block, add an else block (this else is associated with the outer if). Inside this else block, print "Access denied. Must be at least 18 years old.".
```python
if age >= 18:
    if membership == "yes":
        print("Access granted.")
    else:
        print("Membership required for access.")
else:
    print("Access denied. Must be at least 18 years old.")
```

   5. Complete Code: Combine the steps above to form the complete program.
   6. Run the code: Execute your Python code.
   7. Observe the output: 
      - If temperature is greater than 30, you should see the message printed.
      - If temperature is 30 or less, nothing will be printed.
     
   8. (Optional) Input Validation: Add a try-except block to handle potential ValueError if the user enters non-integer input for age.
```python
try:
    #your code here

except ValueError:
    print("Invalid age input. Please enter an integer.")
```


   **Conclusion**
   This exercise demonstrated how to use nested if...else statements to create more complex decision-making structures. You learned how inner if statements depend on the conditions of outer if statements and the importance of correct indentation.  You also practiced handling string input, performing case-insensitive comparisons, and (optionally) adding input validation. Nested if...else statements are essential for building programs that can handle multiple levels of conditions and make more nuanced decisions.

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
   Open the terminal and run:
   
```bash
git status
```
   This command shows any modified or new files.
   
2. Stage the changes:
   Add all modified files to staging:
   
```bash
git add .
```
   
3. Commit your changes:
   Write a meaningful commit message:
   
```bash
git commit -m "Submitting Python Week 04 - Laboratory # 11"
```
   
4. Push your changes to GitHub:
   Upload your changes to your remote repository:
   
```bash
git push origin main
```
