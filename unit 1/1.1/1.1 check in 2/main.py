num = int(input("Enter a number: "))
i = 1

while num > i:
    if num % i == 0:
        print("The number is divisible by", i)
    
    i += 1