for i in range(1,101): #This loop iterates through numbers from 1 to 100.
    output ="" #Initializes an empty string called output.
    if i%3 == 0: #If i is divisible by 3, append "Fizz" to the output string.
     output += "FIZZ"
    if i%5 == 0: #If i is divisible by 5, append "Buzz" to the output string.
     output += "BUZZ"
    print(output or i) 
    """
    If output is not an empty string (meaning it contains "Fizz", "Buzz", or "FizzBuzz"), it will be printed. If output is empty (meaning i was not divisible by 3 or 5), it prints the number i.
    """
