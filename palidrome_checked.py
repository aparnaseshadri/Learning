def is_palidrome(s):
    """
    Check if a given string is a palidrome
    Args:
    s(str) is string to be checked
    Returns:
    bool: True is s is a palidrome, false otherwise
    """
    
    #Remove spaces and convert it to lower cases for comaprison
    s = s.replace(" ","").lower()
    
    #compare the string with its reverse
    return s == s[::-1]

def main():
    print ("Palidrome Checker")
    
    #Interactive input
    user_input = input("Enter the String to check if it is a palidrome")
    if is_palidrome(user_input):
        print ("The given string is a palidrome")
    else:
        print("The given string is not a palidrome")

if __name__  == "__main__":
    main()

    
    
    
    
