# Function to convert decimal to binary

def decimal_to_binary(decimal_number):
   return bin (decimal_number).replace("0b", "")
# Input from the user
decimal_number = int(input("Enter a decimal number: "))
# Convert to binary and display the result
binary_number = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is {binary_number}")