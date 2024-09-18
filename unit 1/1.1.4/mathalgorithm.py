# get two numbers from user
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

# loop while the numbers are not divisible (the remainder is not 0)
while a % b != 0:
  # inform user of result 
  print("The numbers aren't divisible")
  # gather user input again
  a = int(input("Enter your first number again: "))
  b = int(input("Enter your second number again: "))
  
# inform user of result
print("The numbers are divisible")