# Function to subtract two numbers
def subtract_two_numbers(num1, num2):
    if (num1 == 0 and num2 == 0):
        return 0
    
    elif (num1 == 0):
        return -num2
    
    elif (num2 == 0 ):
        return num1
    
    else:
        return num1 - num2
    
# Testing the function
print(subtract_two_numbers(10, 2))
print(subtract_two_numbers(0, 0))
print(subtract_two_numbers(0, 2))
print(subtract_two_numbers(10, 0))
print(subtract_two_numbers(1, 2))