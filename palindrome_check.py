def is_palindrome(s):
    """
    Check if a given string is a palindrome
    Args:
    s(str) is string to be checked
    Returns:
    bool: True is s is a palindrome, false otherwise
    """
    
    #Remove spaces and convert it to lower cases for comaprison
    s = s.replace(" ","").lower()
    
    #compare the string with its reverse
    return s == s[::-1]

def main():
    print ("Palindrome Checker")
    
    #Interactive input
    user_input = input("Enter the String to check if it is a palindrome")
    if is_palidrome(user_input):
        print ("The given string is a palindrome")
    else:
        print("The given string is not a palindrome")

if __name__  == "__main__":
    main()

    
    
    
    
