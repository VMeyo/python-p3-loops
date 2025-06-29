# Function to print happy new ear after decrementing from 10 to 1

def happy_new_year():
    count = 10 # Count should start from 10
    while count > 0: # Sequence should oroceed as long as count is greater than 0
        print(count)
        count -= 1 # Decrement from 10 to 1

    print("Happy New Year!") # Print happy new ear after the sequence is done

# Function to print the square of integers

def square_integers(int_list): # Takes in a list as the argument
    return [num ** 2 for num in int_list] # Use list comprehension to square the numbers
    
    
# Function that checks on multiples of 3 & 5

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)    

    
