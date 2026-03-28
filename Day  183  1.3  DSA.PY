n = int(input())
if n < 100 or n > 999:
    print("Invalid Number")
else:
    middle_digit = (n // 10) % 10
    
    if middle_digit % 3 == 0:
        print("Trendy Number")
    else:
        print("Not a Trendy Number")